# coding=utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from Users.views import phoneValid, hashstr
from Users.models import Users


def loginValid(fun):
    def inner(request, *args, **keywords):
        #id = request.COOKIES.get('userid')
        #name = request.COOKIES.get('username')
        phone = request.session.get('phone')
        if not phone:
            return HttpResponseRedirect('/login/')
        return fun(request, *args, **keywords)
    return inner


def login(request):
    if request.method == 'POST' and request.POST:
        phone = request.POST['logname']
        password = request.POST['logpass']
        validate = phoneValid(phone)
        if not validate['status']:  # 如果用户名存在
            info = validate['data']
            hash_password = hashstr(password)
            user_password = info.password
            if hash_password == user_password:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('user_id', info.id, 3600)
                response.set_cookie('user_name', info.user, 3600)
                request.session['phone'] = info.phone
                return response
        else:
            return HttpResponseRedirect('/login/')
    return render(request, 'login.html', locals())

@loginValid
def index(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = Users.objects.get(id=userid)
    except:
        return HttpResponseRedirect('/login/')
    return render_to_response('index.html', locals())


def logout(request):
    del request.COOKIES['user_id']
    del request.COOKIES['user_name']
    del request.session['phone']
    return HttpResponseRedirect('/login/')

