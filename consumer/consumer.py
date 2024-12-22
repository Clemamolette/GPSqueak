#!/bin/python3
# Python script to consume coordinates from the Kafka topic and interact with the database.
from kafka import KafkaConsumer
import psycopg2
import json
import time
import logging

LOG = logging.Logger("Consumer")

# Function to insert data into the database
def insert_data(coordinate):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = """
        INSERT INTO coordinates (ip, latitude, longitude, t_stamp)
        VALUES (%s, %s, %s, %s)
        """

        # Execute the query
        cursor.execute(insert_query, (coordinate['ip'], coordinate['latitude'], coordinate['longitude'], coordinate['timestamp']))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        LOG.info("Data inserted successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error: {error}")



retries = 5


while retries >= 0:
    try:
        LOG.info("Trying connection with kafka...")
        consumer = KafkaConsumer('coordinate_from_tracker',
                                bootstrap_servers=['kafka:9092'],
                                group_id='coord-to-db',
                                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                                )
        break
    except Exception as e:
        retries -= 1
        LOG.warning(f"Fail to connect ({e}), retrying in 5 seconds...")
        time.sleep(5)

if retries < 0:
    LOG.error("Fail to connect to broker!")
    exit(1)
    
LOG.info("Connected to kafka!")

# Database connection parameters
db_params = {
    'dbname': 'gps_db',
    'user': 'user',
    'password': 'pass',
    'host': 'postgresql',
    'port': '5432'
}



for message in consumer:
    coordinate = message.value
    coordinate['timestamp'] = message.timestamp
    insert_data(coordinate)