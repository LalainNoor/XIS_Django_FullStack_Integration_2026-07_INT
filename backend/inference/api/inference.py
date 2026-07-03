import cv2
import numpy as np
import time

from inference.utils.logger import logger
from inference.mqtt.instance import mqtt_client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inference.services.instance import engine

class InferenceAPIView(APIView):
    """
    Perform image classification using the ONNX model.
    """

    def post(self, request):

        if "image" not in request.FILES:
            return Response(
                {
                    "status": "error",
                    "message": "No image uploaded."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            image_file = request.FILES["image"]

            image_bytes = np.frombuffer(
                image_file.read(),
                np.uint8
            )

            image = cv2.imdecode(
                image_bytes,
                cv2.IMREAD_COLOR
            )

            # Start timer
            start_time = time.perf_counter()

            result = engine.predict(image)
            mqtt_client.publish(
                 {
                    "prediction": result["prediction"],
                    "confidence": result["confidence"],
                     "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

            logger.info(
                f"Prediction={result['prediction']} Confidence={result['confidence']}"
            )

            # Calculate processing time (milliseconds)
            processing_time = (time.perf_counter() - start_time) * 1000

            return Response(
                {
                    "status": "success",
                    "prediction": result["prediction"],
                    "confidence": result["confidence"],
                    "processing_time_ms": round(processing_time, 2),
                    "model": engine.model_path.name,
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            logger.exception(str(e))   
            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )