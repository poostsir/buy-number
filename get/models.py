from django.db import models

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    def __str__(self):
        return self.ip_address

