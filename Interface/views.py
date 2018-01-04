# coding=utf-8
from MyCmdb.views import loginValid
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render_to_response
from Server.models import Servers
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from Users.models import UserProfile


@loginValid
def websockestatus(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    websockinfo = Servers.objects.all()
    interface_name = "websocket"
    return render_to_response('interface/websocket.html', locals())

@csrf_exempt
def interface_restart(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    res = {'status': 'error', 'msg': '请求参数不能为空'}
    if request.method == 'POST' and request.POST:
        serverid = request.POST['id']
        interfacename = request.POST['interface']
        serverip = Servers.objects.get(id=int(serverid)).ip

        res = {'status': 'success', 'msg': '执行重启操作'}
        return JsonResponse(res)
    return JsonResponse(res)