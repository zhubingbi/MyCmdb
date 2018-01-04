# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from models import Loginlog, Serverlog, Toollog
from Users.models import UserProfile
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from MyCmdb.views import loginValid


def login_logs(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')

    platform_isactive = 'active'
    logs_active = 'active'
    login_log = Loginlog.objects.order_by('-ctime')
    return render_to_response('platform/login_log.html', locals())


def server_logs(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    platform_isactive = 'active'
    logs_active = 'active'
    server_log = Serverlog.objects.order_by('-ctime')
    return render_to_response('platform/server_log.html', locals())


def tool_logs(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    platform_isactive = 'active'
    logs_active = 'active'
    tool_log = Toollog.objects.order_by('-ctime')
    return render_to_response('platform/tool_log.html', locals())
