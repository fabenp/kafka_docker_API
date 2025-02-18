from kafka import KafkaConsumer
from influxdb import InfluxDBClient
#import datetime
from datetime import datetime, timezone
import json



#kafka configuration
KAFKA_BROKER = "kafka:9092"
TOPIC= "api-data"

# Kafka Consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    api_version=(0,11,5),
    auto_offset_reset="earliest",  # Start from the beginning
    value_deserializer=lambda v: json.loads(v.decode("utf-8")) # deserialize JSON data
)
# InfluxDB Config
influx_client = InfluxDBClient(host="influxdb", port=8086, database="kafkadb")


for message in consumer:
    data=message.value
    timestamp = data.get("t", datetime.now(timezone.utc).timestamp())
    price=data.get("c",0)
    print("received from kafka:", data)
     # Convert timestamp to nanoseconds for InfluxDB
    timestamp_ns = int(timestamp * 1e9)

    # Format data for InfluxDB
    influx_data = [
        {
            "measurement": "stock_price",
            "tags": {"symbol": "AAPL"},
            "time": int(timestamp * 1e9),  # Convert to nanoseconds
            "fields": {"price": float(price)}
        }
    ]

    # Send data to InfluxDB
    success = influx_client.write_points(influx_data)
    
    if success:
        print("✅ Data inserted into InfluxDB")
    else:
        print("❌ Failed to insert data into InfluxDB")






