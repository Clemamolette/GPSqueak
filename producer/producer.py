# Python script to produce coordinates to the Kafka topic.

from kafka import KafkaProducer
import time
import os
import logging

from generate_coordinate import Coordinate

LOG = logging.getLogger()

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

ip = os.environ.get('PRODUCER_IP')
LOG.info(ip)

# first coordinate
coordinate = Coordinate.generate_coordinate(ip)

while True:
    producer.send('coordinate_from_tracker', coordinate.json())
    coordinate.next_coordinate()
    time.sleep(1)
    
    