from django.db import models
from datetime import date, timedelta


class secret(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    expired = models.BooleanField(default=False)
    uuid = models.CharField(max_length=120, default='uuidtest')
    access_code = models.CharField(default='default_access_code', max_length=120)

    def __str__(self):
        return self.name
