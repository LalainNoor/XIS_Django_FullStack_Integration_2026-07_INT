from django.urls import re_path

from .consumers import InferenceConsumer

websocket_urlpatterns = [
    re_path(r"ws/inference/$", InferenceConsumer.as_asgi()),
]