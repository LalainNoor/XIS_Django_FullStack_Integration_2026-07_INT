import json

from channels.generic.websocket import WebsocketConsumer


class InferenceConsumer(WebsocketConsumer):
    """
    Handles WebSocket connections for live inference.
    """

    def connect(self):
        self.accept()

        self.send(
            text_data=json.dumps(
                {
                    "status": "connected",
                    "message": "WebSocket connected successfully."
                }
            )
        )

    def disconnect(self, close_code):
        print(f"WebSocket disconnected: {close_code}")

    def receive(self, text_data):
        self.send(
            text_data=json.dumps(
                {
                    "status": "success",
                    "received": text_data
                }
            )
        )