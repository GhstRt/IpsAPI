from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import IPSRule
from api.serializers import RuleSerializer


class GetRules(APIView):
    def get(self, request, rule_id=None):
        data = IPSRule.objects.all() if rule_id is None else IPSRule.objects.filter(id=rule_id)
        serializer = RuleSerializer(data, many=True)
        return Response(serializer.data)
