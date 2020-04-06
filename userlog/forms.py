from django.forms import ModelForm, DateInput, TimeInput
from django.forms import DateTimeInput

from .models import UserTimeLog


class UserLogDateInput(DateInput):
    input_type = "date"


class UserLogTimeInput(TimeInput):
    input_type = "time"


class UserTimeLogForm(ModelForm):
    class Meta:
        model = UserTimeLog
        fields = ["username", "title", "description", "date", "start_time", "end_time"]
        widgets = {
            "date": UserLogDateInput,
            "start_time": UserLogTimeInput,
            "end_time": UserLogTimeInput,
        }
