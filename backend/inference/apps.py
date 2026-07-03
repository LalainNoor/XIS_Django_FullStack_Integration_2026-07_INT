from django.apps import AppConfig


class InferenceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inference"

    def ready(self):
        from inference.mqtt.instance import mqtt_client

        try:
            mqtt_client.connect()
            print("MQTT client initialized successfully.")
        except Exception as e:
            print(f"MQTT initialization failed: {e}")