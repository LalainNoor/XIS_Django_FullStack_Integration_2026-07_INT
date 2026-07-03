from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckAPIView(APIView):
    """
    Simple API to verify that the Django REST application is working.
    """

    def get(self, request):
        return Response(
            {
                "status": "success",
                "message": "AI Inference API is running."
            },
            status=status.HTTP_200_OK
        )