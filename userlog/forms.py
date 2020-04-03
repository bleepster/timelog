from django.forms import ModelForm, DateInput, TimeInput
from django.forms import DateTimeInput

from .models import UserTimeLog


class DateInput(DateInput):
    input_type = "date"


class TimeInput(TimeInput):
    input_type = "time"


class UserTimeLogForm(ModelForm):
    class Meta:
        model = UserTimeLog
        fields = ["username", "title", "description", "date", "start_time", "end_time"]
        widgets = {
            "date": DateInput,
            "start_time": TimeInput,
            "end_time": TimeInput,
        }
