# coding=utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from Users.models import UserProfile
from django.contrib.auth.models import User
from Platform.models import Loginlog

from urllib import urlopen


def loginValid(fun):
    """
    验证请求是否携带session
    :param fun:
    :return:
    """
    def inner(request, *args, **keywords):
        #id = request.COOKIES.get('userid')
        #name = request.COOKIES.get('username')
        is_login = request.session.get('is_login')
        if not is_login:
            return HttpResponseRedirect('/login/')
        return fun(request, *args, **keywords)
    return inner


def login(request):
    """
    平台登录url: /login
    :param request:
    :return:
    """
    if request.method == 'POST' and request.POST:
        username = request.POST['logname']
        password = request.POST['logpass']
        user = authenticate(username=username, password=password)
        # 验证用户，密码是否正确
        # validate = phoneValid(phone)
        if user is not None:  # 如果用户名存在
            user_id = (UserProfile.objects.get(id=User.objects.get(username=username).id)).id
            if user.is_active:
                auth_login(request, user)
                response = HttpResponseRedirect('/index/')
                request.session['is_login'] = True
                response.set_cookie('user_id', user_id, 3600)
                login_ip = request.META['REMOTE_ADDR']
                Loginlog.objects.create(user=request.user, ip=login_ip)
                return response
            else:
                error_msg = '用户已被禁用,请联系管理员'
                return render(request, 'login.html', locals())
        else:
            error_msg = '用户名或密码错误,请重试'
            return render(request, 'login.html', locals())
    else:
        return render(request, 'login.html', locals())


@loginValid
def index(request):
    """
    首页url: /index
    :param request:
    :return:
    """
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except:
        return HttpResponseRedirect('/login/')
    return render_to_response('index.html', locals())


def logout(request):
    """
    注销平台登录url: /logout
    :param request:
    :return:
    """
    del request.COOKIES['user_id']
    del request.session['is_login']
    return HttpResponseRedirect('/login/')

