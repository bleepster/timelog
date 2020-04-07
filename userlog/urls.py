from django.urls import path

from .views import userlog, create

urlpatterns = [
    path("", userlog, name="userlog"),
    path("<int:log_id>", userlog, name="userlog"),
    path("create", create, name="create"),
]
