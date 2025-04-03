## AWS IoT MQTT Simulator

This project simulates environmental sensor data (temperature, humidity, and CO₂) and publishes it securely to AWS IoT Core using the MQTT protocol.

# Features
- Simulates real-time environmental sensor readings.
- Publishes data to AWS IoT Core over a TLS-secured MQTT connection.
- Integrates with AWS IoT Analytics for data processing and visualization.

# Technologies Used
- Python
- paho-mqtt
- AWS IoT Core
- AWS IoT Analytics

# File Structure

- 'mqtt_aws_simulator.py': Python script that simulates and publishes sensor data.
- Certificate files (not included in this repo) must be downloaded from AWS IoT:
  - 'AmazonRootCA1.pem'
  - '*.pem.crt' (device certificate)
  - '*.pem.key' (private key)


## Setup Instructions

1. Clone the repository
   - git clone https://github.com/Daivik-Gangappa/aws-iot-mqtt-simulator-2.git
   - cd aws-iot-mqtt-simulator-2 

2. Install Dependencies
   - pip install paho-mqtt

3. Set Up AWS IoT Core
   - Create a Thing in AWS IoT Core.
   - Download the certificate, private key, and root CA.
   - Note your AWS IoT endpoint (e.g., 'your-endpoint-ats.iot.region.amazonaws.com').

4. Edit Certificate Paths in Script
   - In 'mqtt_aws_simulator.py', update the following lines:
   	CA = "path/to/AmazonRootCA1.pem"
   	CERT = "path/to/your-certificate.pem.crt"
   	KEY = "path/to/your-private.pem.key"
   
5. Run the Simulator
   - python mqtt_aws_simulator.py

   
##  MQTT Topic
   - iot/environment/dht1


##  AWS IoT Analytics Configuration

1. Create a Rule in AWS IoT Core:
   - Name: 'RouteSensorData'
   - SQL Query:
     	SELECT * FROM 'iot/environment/dht1'
     
2. Set Up IoT Analytics:
   - Channel: Collects incoming data.
   - Pipeline: Routes data from channel to datastore.
   - Data Store: Stores the processed JSON data.
   - Dataset: Used to run SQL queries and preview data.


##  Reflection

This project provided hands-on experience with secure MQTT communication and real-time IoT data processing using AWS services. Challenges with certificate configuration were overcome, leading to successful data publication and analytics integration.



Author: Daivik Gangappa  
