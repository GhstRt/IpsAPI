from rest_framework.views import APIView
from rest_framework.response import Response


class GetStatus(APIView):
    def get(self, request):
        return Response({"status": {"code": 0, "message": "Proxy Aktif"}})
