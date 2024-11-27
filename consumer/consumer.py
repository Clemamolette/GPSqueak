# Python script to consume coordinates from the Kafka topic and interact with the database.



# !!! NOT TESTED !!!


from kafka import KafkaConsumer
import psycopg2
import json

consumer = KafkaConsumer('COORDINATE',
                         bootstrap_servers=['localhost:8080'],
                         #auto_offset_reset='earliest',
                         #enable_auto_commit=True,
                         #group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))


# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # e.g., 'localhost'
    'port': '8080'   # e.g., '5432'
}

# Function to insert data into the database
def insert_data(coordinate):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = """
        INSERT INTO coordinates (ip, x, y)
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