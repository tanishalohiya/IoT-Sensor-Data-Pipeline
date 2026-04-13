import paho.mqtt.client as mqtt
import time
import random
import json

# Broker Configuration
broker = "broker.hivemq.com"
port = 1883
topic = "iot/sensor/data"

# MQTT Client Setup
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to HiveMQ Broker!")
    else:
        print(f"❌ Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print("📡 Data published successfully!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to Broker
print("Connecting to HiveMQ...")
client.connect(broker, port, 60)
client.loop_start()

# Simulate IoT Sensor Data
try:
    while True:
        data = {
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": round(random.uniform(40, 80), 2),
            "timestamp": time.strftime("%H:%M:%S"),
            "sensor_id": "SENSOR-01",
            "location": "Lab Room 1"
        }

        client.publish(topic, json.dumps(data))
        print(f"📤 Sent: {data}")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
    client.loop_stop()
    client.disconnect()
    print("✅ Disconnected cleanly")