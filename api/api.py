# Python script to serve the front-end API.

from fastapi import FastAPI
import db_tools as db
app = FastAPI()

db_params = {
    'dbname': 'gps_db',
    'user': 'user',
    'password': 'pass',
    'host': 'postgresql',
    'port': '5432'
}

# TODO gerer le cas ou la base n'existe pas 
db_connection, cursor = db.connect(db_params)

@app.get("/position/{id}/all")
def get_all_position(id : str) -> dict:
    res = db.fetch_all_positions(id, cursor)
    print(res)
    return res

@app.get("/position/{id}")
def get_position(id : str) -> dict:
    res = db.fetch_last_position(id, cursor)
    print(res)
    return res

@app.get("/id")
def get_ip() -> dict:
    """fetch all mice ips"""
    res = db.fetch_ip_list(cursor)
    print(res)
    return res

@app.get("/name")
def get_name() -> dict:
    """fetch all mice names"""
    res = db.fetch_name_list(cursor)
    print(res)
    return res

@app.get("/ip/{mouse}")
def get_ip_of(mouse : str) -> dict:
    """fetch the requested mouse's ip"""
    res = db.fetch_ip_from_name(mouse, cursor)
    print(res)
    return res
    pass