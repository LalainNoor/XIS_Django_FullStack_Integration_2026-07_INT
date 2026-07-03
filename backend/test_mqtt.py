import time

from inference.mqtt.mqtt_client import MQTTClient


def main():

    mqtt_client = MQTTClient()

    mqtt_client.connect()

    time.sleep(2)

    mqtt_client.publish(
        {
            "prediction": "forest",
            "confidence": 99.98,
            "status": "success"
        }
    )

    print("Waiting for subscribed message...")

    time.sleep(5)


if __name__ == "__main__":
    main()