from django.db import models


class NetworkLog(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=70, verbose_name="Client Address")
    server = models.CharField(max_length=70, verbose_name="Server Address")
    port = models.IntegerField(verbose_name="Port Number")
    protocol = models.CharField(max_length=20, verbose_name="Transport Protocol")
    tls = models.BooleanField(verbose_name="Has TLS", default=False)
    size = models.IntegerField(verbose_name="Content Size")
    action = models.CharField(max_length=20, verbose_name="Action Type")
