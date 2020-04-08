from django.forms import Form
from django.forms import (
    ModelForm,
    DateInput,
    TimeInput,
    EmailInput,
    TextInput,
    Textarea,
    EmailField,
)

from .models import UserTimeLog


class UserLogDateInput(DateInput):
    input_type = "date"


class UserLogTimeInput(TimeInput):
    input_type = "time"


class UserTimeLogForm(ModelForm):
    class Meta:
        model = UserTimeLog
        fields = (
            "username",
            "title",
            "description",
            "date",
            "start_time",
            "end_time",
        )
        widgets = {
            "username": EmailInput(
                attrs={"class": "form-control", "placeholder": "User Name"}
            ),
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "description": Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
            "date": UserLogDateInput(attrs={"class": "form-control"}),
            "start_time": UserLogTimeInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "end_time": UserLogTimeInput(
                attrs={"class": "form-control form-control-sm"}
            ),
        }


class SearchTimeLogForm(Form):
    username = EmailField(
        widget=EmailInput(attrs={"class": "form-control", "placeholder": "User Name"})
    )
