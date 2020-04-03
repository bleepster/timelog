from django.urls import path

from .views import userlog

urlpatterns = [
    path("", userlog, name="userlog"),
]
