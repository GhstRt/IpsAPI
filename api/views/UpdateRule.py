from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import IPSRule


class UpdateRule(APIView):
    def put(self, request, rule_id=None):
        rule_name = request.data["rule_name"]
        rule_type = request.data["rule_type"]
        description = request.data["description"]
        address = request.data["address"]
        pattern = request.data["pattern"]
        threshold = request.data["threshold"]
        action = request.data["action"]

        rule = IPSRule.objects.get(id=rule_id)
        rule.rule_name = rule_name
        rule.rule_type = rule_type
        rule.description = description
        rule.address = address
        rule.pattern = pattern
        rule.threshold = threshold
        rule.action = action

        rule.save()

        return Response({"status": {"code": 0, "message": "success"}}, status.HTTP_200_OK)
