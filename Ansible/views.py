from django.shortcuts import render
from django.shortcuts import render_to_response
from Server.models import Servers
from Users.models import Users
# Create your views here.


def hostlist(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    serverList = Servers.objects.all()
    return render_to_response('hostlist.html', locals())