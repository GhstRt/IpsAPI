from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User
from api.serializers import UserSerializer


class GetUsers(APIView):
    def get(self, request, user_id=None):
        data = User.objects.all() if user_id is None else User.objects.filter(id=user_id)
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
