from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import IPSRule


class DeleteRule(APIView):
    def delete(self, request, rule_id=None):
        rule = IPSRule.objects.get(id=rule_id)
        rule.delete()
        return Response({"status": {"code": 0, "message": "success"}}, status.HTTP_200_OK)
