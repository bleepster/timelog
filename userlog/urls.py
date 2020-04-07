from django.urls import path

from .views import userlog, add

urlpatterns = [
    path("", userlog, name="userlog"),
    path("<int:log_id>", userlog, name="userlog"),
    path("add", add, name="add"),
]
