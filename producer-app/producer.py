from kafka import KafkaProducer
import json
import time
import random
import requests

#kafka configuration
KAFKA_BROKER= "kafka:9092"
TOPIC= "api-data"

#create kafka producer:
producer =KafkaProducer(bootstrap_servers=KAFKA_BROKER,api_version=(0,11,5),value_serializer=lambda v: json.dumps(v).encode("utf-8"))

#get data from API

API_KEY="##############"
SYMBOL= "AAPL"
URL=f"https://finnhub.io/api/v1/quote?symbol={SYMBOL}&token={API_KEY}"

def fetch_data():
    response= requests.get(URL)
    if response.status_code == 200: # check if it was successful
        return response.json()
    #print("stock data", data)
    else:
        print(f"error {response.status_code}:{response.text}")
        return None

#send data periodically
while True:
    data =fetch_data()
    if data:
        producer.send(TOPIC,data)
        print("sent to kafka", data)
    time.sleep(10)
