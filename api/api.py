# Python scridt to serve the front-end API.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db_tools as db
import time
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8084",
    "http://localhost:8083",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




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
def get_all_position(id : str) -> list:
    res = db.fetch_all_positions(id, cursor)
    return res

@app.get("/position/{id}")
def get_position(id : str) -> list:
    res = db.fetch_last_position(id, cursor)
    return res

@app.get("/id")
def get_id() -> dict:
    """fetch all mice ids"""
    res = db.fetch_id_list(cursor)
    return res
