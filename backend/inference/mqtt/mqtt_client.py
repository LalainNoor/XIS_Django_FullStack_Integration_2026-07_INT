import json
import time

import paho.mqtt.client as mqtt

from inference.utils.logger import logger


class MQTTClient:
    """
    MQTT Client for publish/subscribe communication.
    """

    def __init__(self):

        self.connected = False

        self.broker = "broker.emqx.io"
        self.port = 1883
        self.topic = "xis/inference/results"

        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        """
        Connect to MQTT broker.
        """

        self.client.connect(self.broker, self.port, 60)

        self.client.loop_start()

        while not self.connected:
            time.sleep(0.1)

    def on_connect(
        self,
        client,
        userdata,
        flags,
        reason_code,
        properties=None,
    ):
        """
        Called after successful connection.
        """

        self.connected = True

        logger.info("MQTT Connected")

        print("MQTT Connected")

        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        """
        Receive subscribed messages.
        """

        message = msg.payload.decode()

        logger.info(f"Received: {message}")

        print(f"Received: {message}")

    def publish(self, data):
        """
        Publish prediction data.
        """

        payload = json.dumps(data)

        self.client.publish(self.topic, payload)

        logger.info(f"Published: {payload}")

        print(f"Published: {payload}")