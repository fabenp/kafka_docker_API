# Data pipeline with kafka and Docker with API


This is a simple project with a pipeline in Docker using kafka to import data from an API , influxDB to store it and grafana to visualize it 

the data source is finnhub. A free API key can be requested 


finnhub (API) --> Producer (generate data)---> broker--->consumer--> InfluxDB ----> Grafana

All this pipeline is inside docker with the following containers:
- zookeeper
- kafka
- producer
- consumer
- influxdb
- grafana
  

folder structure :

- docker-compose.yml
- producer-app
  - consumer.py
  - Dockerfile
  - requirements.txt
- consumer-app
  - consumer.py
  - Dockerfile
  - requirements.txt
- grafana_provisioning
   - datasources.yml
- kafka
    - server.properties

how to start:

start docker Desktop (install it if you don't have it)
request a key to run API from finnhub
from your project folder run in cmd: docker-compose up -d

Install libraries : pip install kafka-python requests




InfluxDB:

how to visualize:
Use docker exec -it influxdb influx to open InfluxDB.
Run SHOW DATABASES; to list databases.
use "database"
Use SHOW MEASUREMENTS; to list tables.
SELECT * FROM "semeasurment" LIMIT 10;


Grafana:

Check Grafana at http://localhost:3000 for visualizations.
URL: http://influxdb:8086 # since influxdb and grafana are both inside docker (if influxdb outside of docker http://localhost:8086)
under dashboard creation, use the command : SELECT * from  stock_price, and the table mode

Debugging:
if you have previous containers with the same name as the ones in this project, it is possbile that they won't start with the error message stating  a conflict
you need to remove them first and then restart docker-compose

if an error indicate that requirements.txt files are not found, make sur to not add .txt while creating a txt file. it will add automatically

Key	    Description
c    	Current price (latest stock price)
d		Change (price difference from previous close)
dp		Percentage change (relative to previous close)
h		High price (highest price in the current session)
l		Low price (lowest price in the current session)
o		Open price (stock price at market open)
pc		Previous close (closing price of the last session)
t		Timestamp (Unix epoch time of the latest data)

added ,api_version=(0,11,5) to KafkaProducer
