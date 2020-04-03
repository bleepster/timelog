from django.db import models
from django.utils.timezone import now


class UserTimeLog(models.Model):
    username = models.EmailField()
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(default=now)
    start_time = models.TimeField()
    end_time = models.TimeField()
