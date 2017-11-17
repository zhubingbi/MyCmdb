from django.shortcuts import render
from django.shortcuts import render_to_response
from Server.models import Servers
from Users.models import Users
from .models import toolscript
from .forms import ToolForm
# Create your views here.


def hostlist(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    serverList = Servers.objects.all()
    return render_to_response('hostlist.html', locals())


def tools(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    obj = toolscript.objects.all()
    return render_to_response('tools/tools.html', locals())


def addtools(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'POST' and request.POST:
        form = ToolForm(request.POST)
        if form.is_valid():
            tools_save = form.save()
            form = ToolForm()
            return render_to_response('tools/addtools.html', locals())
    else:
        form = ToolForm()
    return render_to_response('tools/addtools.html', locals())