from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import NetworkLog
from api.serializers import NetworkLogSerializer


class GetLogs(APIView):
    def get(self, request, log_id=None):
        data = NetworkLog.objects.all() if log_id is None else NetworkLog.objects.filter(id=log_id)
        serializer = NetworkLogSerializer(data, many=True)
        return Response(serializer.data)
