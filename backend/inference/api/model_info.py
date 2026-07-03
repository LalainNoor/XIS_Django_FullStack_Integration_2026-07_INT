from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inference.services.inference_engine import InferenceEngine


class ModelInfoAPIView(APIView):
    """
    Returns information about the loaded ONNX model.
    """

    def get(self, request):
        try:
            engine = InferenceEngine()

            return Response(
                engine.get_model_info(),
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