from django.http import HttpResponse, Http404
from django.template import loader

from .models import UserTimeLog
from .forms import UserTimeLogForm


def userlog(request, log_id=None):
    if not log_id:
        logs = UserTimeLog.objects.all()
        template = loader.get_template("table_view.html")
        context = {"logs": logs}
        return HttpResponse(template.render(context, request))
    else:
        try:
            log = UserTimeLog.objects.get(pk=log_id)
            template = loader.get_template("detail_view.html")
            # FIXME: write a better way to transform the values
            context = {
                "log": {
                    v: log.__dict__[k]
                    for k, v in dict(
                        {
                            "username": "User Name",
                            "title": "Title",
                            "description": "Description",
                            "date": "Date",
                            "start_time": "Start Time",
                            "end_time": "End Time",
                        }
                    ).items()
                }
            }
            return HttpResponse(template.render(context, request))
        except UserTimeLog.DoesNotExist:
            raise Http404("Log Does not exist")


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
