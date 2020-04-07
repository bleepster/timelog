from django.db import models
from django.utils.timezone import now


class UserTimeLog(models.Model):
    username = models.EmailField(verbose_name="User Name")
    title = models.CharField(max_length=64, verbose_name="Title")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    date = models.DateField(default=now, verbose_name="Date")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
