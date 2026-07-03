import cv2
import numpy as np
import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inference.services.inference_engine import InferenceEngine


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

            engine = InferenceEngine()

            # Start timer
            start_time = time.perf_counter()

            result = engine.predict(image)

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

            return Response(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )