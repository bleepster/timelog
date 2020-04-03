from django.contrib import admin

# Register your models here.

from .models import UserTimeLog

admin.site.register(UserTimeLog)
