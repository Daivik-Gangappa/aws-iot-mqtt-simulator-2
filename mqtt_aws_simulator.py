import time
import json
import random
import ssl
import paho.mqtt.client as mqtt

# AWS IoT Core Endpoint
AWS_IOT_ENDPOINT = "a3mm3pt1h8soxw-ats.iot.us-east-1.amazonaws.com"
PORT = 8883
TOPIC = "iot/environment/dht1"

# Paths to certificates
CA = "C:/Users/daiwi/Desktop/IOT/InClass_Week10/AmazonRootCA1.pem"
CERT = "C:/Users/daiwi/Desktop/IOT/InClass_Week10/a418d56bd7e212ceac5a11997545a8d0810bec8319a52b17528166026234ebce-certificate.pem.crt"
KEY = "C:/Users/daiwi/Desktop/IOT/InClass_Week10/a418d56bd7e212ceac5a11997545a8d0810bec8319a52b17528166026234ebce-private.pem.key"

# MQTT connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to AWS IoT Core")
    else:
        print(f"Connection failed. Code: {rc}")

# Create client and set credentials
client = mqtt.Client()
client.on_connect = on_connect

client.tls_set(
    ca_certs=CA,
    certfile=CERT,
    keyfile=KEY,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# Connect and start loop
client.connect(AWS_IOT_ENDPOINT, PORT, keepalive=60)
client.loop_start()

# Publish simulated data
while True:
    payload = {
        "temperature": round(random.uniform(-10, 40), 2),
        "humidity": round(random.uniform(20, 90), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }
    print("Publishing:", payload)
    client.publish(TOPIC, json.dumps(payload))
    time.sleep(10)
