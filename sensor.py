import paho.mqtt.client as mqtt
import time
import random
import json

broker = "broker.hivemq.com"
port = 1883
topic = "iot/sensor/data"

client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    client.publish(topic, json.dumps(data))
    print("Sent:", data)

    time.sleep(2)