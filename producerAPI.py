from json import dumps
from kafka import KafkaProducer
import requests
import json


def kafkaProducer(eid):
    if eid == 1:
        updates = ""
        topicName = 'topic1'
        headers = {
            'Accept': 'text/plain',
        }
        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        updates = response.text
        bootstrap_servers = ['localhost:9092', 'localhost:9093', 'localhost:9094']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers, api_version=(2, 0, 2))
        producer.send(topicName, value=updates.encode('utf-8'))
        producer.flush()
        producer.close()
    elif eid == 2:
        updates = ""
        topicName = 'topic2'
        headers = {
            'Accept': 'text/plain',
        }
        response = requests.get("https://api.adviceslip.com/advice", headers=headers)
        jj = json.loads(response.text)
        updates = jj['slip']['advice']
        bootstrap_servers = ['localhost:9092', 'localhost:9093', 'localhost:9094']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers, api_version=(2, 0, 2))
        producer.send(topicName, value=updates.encode('utf-8'))
        producer.flush()
        producer.close()
    elif eid == 3:
        updates = ""
        topicName = 'topic3'
        headers = {
            'Accept': 'text/plain',
        }
        response = requests.get("https://zenquotes.io/api/random", headers=headers)
        jj = json.loads(response.text)
        updates = jj[0]['q']
        bootstrap_servers = ['localhost:9092', 'localhost:9093', 'localhost:9094']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers, api_version=(2, 0, 2))
        producer.send(topicName, value=updates.encode('utf-8'))
        producer.flush()
        producer.close()
    return

