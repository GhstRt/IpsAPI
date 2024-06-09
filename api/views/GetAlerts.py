from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Alert
from api.serializers import AlertSerializer


class GetAlerts(APIView):
    def get(self, request):
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)
