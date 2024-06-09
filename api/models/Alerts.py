from django.db import models
from api.models import NetworkLog


class Alert(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    log = models.ForeignKey(NetworkLog, on_delete=models.CASCADE)
