from django.urls import path

from .views import userlog, create, search

urlpatterns = [
    path("", userlog, name="userlog"),
    path("<int:log_id>", userlog, name="userlog"),
    path("search", search, name="search"),
    path("create", create, name="create"),
]
