# Python script to produce coordinates to the Kafka topic.

from kafka import KafkaProducer
import json
import time
from random import random
import os
import logging

LOG = logging.Logger("Consumer")


class Coord:
    latitude : float
    longitude : float
    ip : str

    def __init__(self, latitude_ : float, longitude_ : float, ip_ : str):
        self.latitude = latitude_
        self.longitude = longitude_
        self.ip = ip_
    

    def getNeighbour(self)->'Coord':
        """
            returns a Coord that is acceptable as a next step from this Coord
        """
        return Coord(self.latitude + 1., self.longitude, self.ip)

    def json(self)->str:
        """
            returns json file of the coords
        """
        dictionnary = {'ip': self.ip, 'latitude': self.latitude, 'longitude': self.longitude}
        return json.dumps(dictionnary).encode('utf-8')


retries = 5


while retries >= 0:
    try:
        LOG.info("Trying connection with kafka...")
        producer = KafkaProducer(bootstrap_servers='kafka:9092', retries=5, max_in_flight_requests_per_connection=1)
        break
    except Exception as e:
        retries -= 1
        LOG.warning(f"Fail to connect ({e}), retrying in 5 seconds...")
        time.sleep(5)
producer = KafkaProducer(bootstrap_servers='kafka:9092', retries=5, max_in_flight_requests_per_connection=1)

ip = os.environ.get('PRODUCER_IP')

# first coordinate
coordinate = Coord(random(), random(), ip)

while True:
    producer.send('coordinate_from_tracker', coordinate.json())
    coordinate = coordinate.getNeighbour()
    time.sleep(1)
    
    