# Python scridt to serve the front-end API.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db_tools as db
import time
import threading

origins = [
    "http://localhost",
    "http://localhost:8084",
    "http://localhost:8083",
    "http://localhost:5173",
]





db_params = {
    'dbname': 'gps_db',
    'user': 'user',
    'password': 'pass',
    'host': 'postgresql',
    'port': '5432'
}


def try_connect(db_connection, db_params):
    while db_connection is None or db_connection.closed != 0:
        db_connection = db.connect(db_params)
        time.sleep(5)
    return db_connection

db_connection = None
db_connection = try_connect(db_connection, db_params)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/position/{id}/all")
def get_all_position(id: str) -> list:
    global db_connection
    if db_connection.closed != 0:
        db_connection = try_connect(db_connection, db_params)
        
    cursor = db_connection.cursor()
    try:
        res = db.fetch_all_positions(id, cursor)
        # print(f"/position/{id}/all =>", res)
        return res
    finally:
        cursor.close()

@app.get("/position/{id}")
def get_position(id: str) -> list:
    global db_connection
    if db_connection.closed != 0:
        db_connection = try_connect(db_connection, db_params)

    cursor = db_connection.cursor()
    try:
        res = db.fetch_last_position(id, cursor)
        # print(f"/position/{id} =>", res)
        return res
    finally:
        cursor.close()

@app.get("/id")
def get_id() -> dict:
    """fetch all mice ids"""
    global db_connection
    if db_connection.closed != 0:
        db_connection = try_connect(db_connection, db_params)

    cursor = db_connection.cursor()
    try:
        res = db.fetch_id_list(cursor)
        # print(f"/id =>", res)
        return res
    finally:
        cursor.close()
