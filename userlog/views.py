from django.http import HttpResponse
from django.template import loader

from .models import UserTimeLog
from .forms import UserTimeLogForm


def userlog(request):
    logs = UserTimeLog.objects.all()
    template = loader.get_template("table_view.html")
    context = {"logs": logs}
    return HttpResponse(template.render(context, request))


def add(request):
    form = UserTimeLogForm()
    if request.method == "POST":
        form = UserTimeLogForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UserTimeLogForm()
    template = loader.get_template("add_form.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))
