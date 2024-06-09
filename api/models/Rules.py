from django.db import models


class IPSRule(models.Model):
    RULE_TYPES = [
        ('tls', 'TLS-based Detection'),
        ('size', 'Size-based Detection'),
        ('proto', 'Protocol-based Detection'),
        ('address', 'Address-based Detection'),
        ('port', 'Port-based Detection'),
    ]

    id = models.AutoField(primary_key=True)
    rule_name = models.CharField(max_length=100)
    rule_type = models.CharField(max_length=10, choices=RULE_TYPES)
    description = models.TextField()
    address = models.CharField(max_length=255)  # İmza veya desen için
    pattern = models.CharField(max_length=255, null=True, blank=True)
    threshold = models.IntegerField(null=True, blank=True)  # Anomali tespiti için eşik değeri
    action = models.CharField(max_length=50)  # Örneğin: 'block', 'alert', 'log'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rule_name
