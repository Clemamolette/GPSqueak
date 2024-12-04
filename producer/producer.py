# Python script to produce coordinates to the Kafka topic.

from kafka import KafkaProducer
import json
import time
from random import random
import os

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

producer = KafkaProducer(bootstrap_servers='localhost:9092', retries=5, max_in_flight_requests_per_connection=1)

ip = "IP1" # os.environ.get('PRODUCER_IP')

# first coordinate
coordinate = Coord(random(), random(), ip)

while True:
    producer.send('coordinate_from_tracker', coordinate.json())
    coordinate = coordinate.getNeighbour()
    time.sleep(1)