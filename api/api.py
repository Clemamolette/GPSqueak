# Python script to serve the front-end API.

from fastapi import FastAPI
import db_tools as db
app = FastAPI()

db_params = {
    'dbname': 'gpsdatabase',
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}
db_connection, cursor = db.connect(db_params)

@app.get("/position/{ip}/all")
def get_all_position(ip : str) -> dict:
    res = db.fetch_all_positions(ip, cursor)
    print(res)
    return res


@app.get("/position/{ip}")
def get_position(ip : str) -> dict:
    res = db.fetch_last_position(ip, cursor)
    print(res)
    return res

@app.get("/ip")
def get_ip() -> dict:
    """fetch all mice ips"""
    pass

@app.get("/name")
def get_name() -> dict:
    """fetch all mice names"""
    pass

@app.get("/ip/{mouse}")
def get_ip_of(mouse : str) -> dict:
    """fetch the requested mouse's ip"""
    pass