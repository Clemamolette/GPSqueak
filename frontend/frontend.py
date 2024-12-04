# Python script to serve the front-end API.

from fastapi import FastAPI
import psycopg2


app = FastAPI()

db_params = {
    'dbname': 'gpsdatabase',
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}
db_connection = psycopg2.connect(**db_params)
cursor = db_connection.cursor()

@app.get("/all_pos/{ip}")
def get_all_pos(ip : str) -> dict:
    query = """
        SELECT * FROM coordinates
        WHERE coordinates.ip = %s
        """
    
    cursor.execute(query, ip)
    query_result = db_connection.commit()
    return query_result

@app.get("/last_pos/{ip}")
def get_last_pos(ip : str) -> dict:
    query = """
        SELECT * FROM coordinates
        WHERE coordinates.ip = %s
        ORDER BY DESC coordinates.id
        LIMIT 1
        """
    
    cursor.execute(query, ip)
    query_result = db_connection.commit()
    return query_result