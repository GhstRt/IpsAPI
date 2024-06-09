from rest_framework import serializers
from api.models import IPSRule


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPSRule
        fields = '__all__'
