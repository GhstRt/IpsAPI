import secrets
import string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.User import User
from api.models.Authentication import Authentication


class Login(APIView):
    def post(self, request):
        ip = request.headers.get("REMOTE_ADDR")
        try:
            username = request.data["username"]
            password = request.data["password"]
            user = User.objects.get(username=username, password=password)
            token = self.generate_random_token(user)
            return Response({"status": {"code": "0", "message": "success"}, "data": {"user": user.username, "token": token}},
                            status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"status": {"code": "1", "message": "Login Error"}, "data": {}}, status=status.HTTP_200_OK)

    def generate_random_token(self, user, length=64):
        alphabet = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(alphabet) for i in range(length))
        auth = Authentication(user=user, token=token)
        auth.save()
        return token
