# Python script to consume coordinates from the Kafka topic and interact with the database.





from kafka import KafkaConsumer
import psycopg2
import json

# !!! NOT TESTED !!!
consumer = KafkaConsumer('COORDINATE',
                         bootstrap_servers=['localhost:8080'],
                         #auto_offset_reset='earliest',
                         #enable_auto_commit=True,
                         #group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))


# TESTED :D
# Database connection parameters
db_params = {
    'dbname': 'gpsdatabase',
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

# Function to insert data into the database
def insert_data(coordinate):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = """
        INSERT INTO coordinates (ip, latitude, longitude)
        VALUES (%s, %s, %s)
        """

        # Execute the query
        cursor.execute(insert_query, (coordinate['ip'], coordinate['latitude'], coordinate['longitude']))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print("Data inserted successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

for message in consumer:
    coordinate = message.value
    insert_data(coordinate)