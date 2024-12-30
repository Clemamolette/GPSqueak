#!/bin/python3
# Python script to consume coordinates from the Kafka topic and interact with the database.
from kafka import KafkaConsumer
import psycopg2
from psycopg2 import sql
import json
import time
import logging
import random
from datetime import datetime

LOG = logging.Logger("Consumer")

noms_de_souris = [
    "Mickey",
    "Minnie",
    "Squeaky",
    "Whiskers",
    "Nibbles",
    "Cheesy",
    "Speedy",
    "Grey",
    "Brownie",
    "Tiny"
]


def insert_coord(id,lat,long,timestamp,cursor):
    
    try:
        # SQL query to insert data
        insert_query = """
        INSERT INTO coordinates (id_mouse, latitude, longitude, t_stamp)
        VALUES (%s, %s, %s, %s) 
        """
        t_stamp = datetime.fromtimestamp(timestamp / 1000.0)
        # Execute the query
        
        cursor.execute(insert_query, (id,lat,long,t_stamp))
        conn.commit()
        
        LOG.info("Coord inserted successfully!")
    
    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error new coord: {error}")


# Function to insert data into the database
def insert_data(coordinate,cursor):
    try:
        query = sql.SQL("SELECT * FROM mouses WHERE ip = %s")

        cursor.execute(query, (coordinate['ip'],))

        # Récupérer le résultat
        result = cursor.fetchone()
    
    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error mouse exist ?: {error}")
        return
    
    if not result:
        try:
            # SQL query to insert data
            insert_query = sql.SQL("INSERT INTO mouses (ip, name) VALUES (%s, %s) RETURNING id;")

            nb = random.randint(0,1000)
            s = random.choice(noms_de_souris)

            # Execute the query
            cursor.execute(insert_query, (coordinate['ip'],s+str(nb)))
            conn.commit()

            # Commit the transaction
            result = cursor.fetchone()

            LOG.info("Mouse inserted successfully!")

        except (Exception, psycopg2.DatabaseError) as error:
            LOG.error(f"Error new mouse: {error}")
            return

    insert_coord(result[0], coordinate['latitude'], coordinate['longitude'], coordinate['timestamp'],cursor)


consumer = None
while consumer is None:
    try:
        LOG.info("Trying connection with kafka...")
        consumer = KafkaConsumer('coordinate_from_tracker',
                                bootstrap_servers=['kafka:9092'],
                                group_id='coord-to-db',
                                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                                )
        break
    except Exception as e:
        LOG.warning(f"Fail to connect ({e}), retrying in 5 seconds...")
        time.sleep(5)
    
LOG.info("Connected to kafka!")

# Database connection parameters
db_params = {
    'dbname': 'gps_db',
    'user': 'user',
    'password': 'pass',
    'host': 'postgresql',
    'port': '5432'
}

def connect(db_params : dict):
    """establishes connection to the database
    
    Keyword arguments:
    db_params -- dictionary of the necessary info to connect to the database ('db_name', 'user', 'password', 'host', 'port')
    Return: None
    """
    
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error: {error}")
        return None

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)

def try_connect(conn, db_params):
    while conn is None or conn.closed != 0:
        conn = connect(db_params)
        time.sleep(5)
    return conn

conn = None
conn = try_connect(conn, db_params)


for message in consumer:
    if conn is None or conn.closed != 0:
        conn = try_connect(conn, db_params)
        
    cursor = conn.cursor()
    coordinate = message.value
    coordinate['timestamp'] = message.timestamp
    try:
        insert_data(coordinate,cursor)
    finally:
        cursor.close()


# Close the cursor and connection
conn.close()