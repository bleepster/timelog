from django.db import models


class UserTimeLog(models.Model):
    username = models.EmailField()
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
