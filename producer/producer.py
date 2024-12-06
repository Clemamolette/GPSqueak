# Python script to produce coordinates to the Kafka topic.

from kafka import KafkaProducer
import time
import os
import logging

from generate_coordinate import Coordinate

LOG = logging.getLogger()


producer = KafkaProducer(bootstrap_servers='kafka:9092', retries=5, max_in_flight_requests_per_connection=1)

ip = os.environ.get('PRODUCER_IP')
LOG.info(ip)

# first coordinate
coordinate = Coordinate.generate_coordinate(ip)

while True:
    producer.send('coordinate_from_tracker', coordinate.next_coordinate().json())
    coordinate = coordinate.getNeighbour()
    time.sleep(1)
    
    