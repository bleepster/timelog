from django.http import HttpResponse
from django.template import loader

from .models import UserTimeLog


def userlog(request):
    logs = UserTimeLog.objects.all()
    template = loader.get_template("table_view.html")
    context = {"logs": logs}
    return HttpResponse(template.render(context, request))
