import time
import json
import paho.mqtt.client as mqtt


class MQTTClient:

    def __init__(self):

        self.connected = False

        self.broker = "broker.emqx.io"
        self.port = 1883
        self.topic = "xis/inference/results"

        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):

        self.client.connect(self.broker, self.port, 60)

        self.client.loop_start()

        while not self.connected:
            time.sleep(0.1)

    def on_connect(self, client, userdata, flags, reason_code, properties=None):

        print("MQTT Connected")

        self.connected = True

        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):

        print(f"Received: {msg.payload.decode()}")

    def publish(self, data):

        payload = json.dumps(data)

        self.client.publish(self.topic, payload)

        print(f"Published: {payload}")