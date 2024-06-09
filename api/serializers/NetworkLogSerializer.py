from rest_framework import serializers
from api.models import NetworkLog


class NetworkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkLog
        fields = '__all__'
