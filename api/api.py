# Python script to serve the front-end API.

from fastapi import FastAPI
import db_tools as db
import time
app = FastAPI()

db_params = {
    'dbname': 'gps_db',
    'user': 'user',
    'password': 'pass',
    'host': 'postgresql',
    'port': '5432'
}

db_connection, cursor = db.connect(db_params)
while db_connection == None:
    time.sleep(5)
    db_connection, cursor = db.connect(db_params)

@app.get("/position/{id}/all")
def get_all_position(id : str) -> dict:
    res = db.fetch_all_positions(id, cursor)
    return res

@app.get("/position/{id}")
def get_position(id : str) -> dict:
    res = db.fetch_last_position(id, cursor)
    return res

@app.get("/id")
def get_ip() -> dict:
    """fetch all mice ips"""
    res = db.fetch_ip_list(cursor)
    return res

@app.get("/name")
def get_name() -> dict:
    """fetch all mice names"""
    res = db.fetch_name_list(cursor)
    return res

@app.get("/id/{mouse}")
def get_ip_of(mouse : str) -> dict:
    """fetch the requested mouse's id"""
    res = db.fetch_ip_from_name(mouse, cursor)
    return res