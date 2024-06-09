from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User


class AddUser(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        name_surname = request.data["name_surname"]

        new_user = User(username=username,
                        password=password,
                        email=email,
                        name_surname=name_surname)

        new_user.save()

        return Response({"status": {"code": 0, "message": "success"}}, status.HTTP_200_OK)
