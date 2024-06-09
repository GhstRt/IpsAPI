from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User


class UpdateUser(APIView):
    def put(self, request, user_id=None):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        name_surname = request.data["name_surname"]

        user = User.objects.get(id=user_id)
        user.username = username
        user.password = password
        user.email = email
        user.name_surname = name_surname

        user.save()

        return Response({"status": {"code": 0, "message": "success"}}, status.HTTP_200_OK)
