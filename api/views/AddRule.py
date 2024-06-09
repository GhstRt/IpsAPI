from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import IPSRule


class AddRule(APIView):
    def post(self, request):
        rule_name = request.data["rule_name"]
        rule_type = request.data["rule_type"]
        description = request.data["description"]
        address = request.data["address"]
        pattern = request.data["pattern"]
        threshold = request.data["threshold"]
        action = request.data["action"]

        new_rule = IPSRule(
            rule_name=rule_name,
            rule_type=rule_type,
            description=description,
            address=address,
            pattern=pattern,
            threshold=threshold,
            action=action
        )

        new_rule.save()

        return Response({"status": {"code": 0, "message": "success"}}, status.HTTP_200_OK)
