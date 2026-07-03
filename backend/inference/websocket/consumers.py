import json

from channels.generic.websocket import WebsocketConsumer

from inference.utils.logger import logger


class InferenceConsumer(WebsocketConsumer):

    def connect(self):

        self.accept()

        logger.info("WebSocket Connected")

        self.send(
            text_data=json.dumps(
                {
                    "status": "connected",
                    "message": "WebSocket connected successfully."
                }
            )
        )

    def disconnect(self, close_code):

        logger.info("WebSocket Disconnected")

    def receive(self, text_data):

        logger.info(f"WebSocket Received: {text_data}")

        self.send(
            text_data=json.dumps(
                {
                    "status": "success",
                    "message": "Message received.",
                    "data": text_data
                }
            )
        )