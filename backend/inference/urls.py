from django.urls import path

from .api.health import HealthCheckAPIView
from .api.model_info import ModelInfoAPIView
from .api.inference import InferenceAPIView

urlpatterns = [
    path("health/", HealthCheckAPIView.as_view(), name="health"),
    path("model-info/", ModelInfoAPIView.as_view(), name="model_info"),
    path("inference/", InferenceAPIView.as_view(), name="inference"),
]