# coding=utf-8
import hashlib
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import AdminUserForm
from PIL import Image
from models import Users
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def loginValid(fun):
    def inner(request, *args, **keywords):
        #id = request.COOKIES.get('userid')
        #name = request.COOKIES.get('username')
        phone = request.session.get('phone')
        if not phone:
            return HttpResponseRedirect('/login/')
        return fun(request, *args, **keywords)
    return inner


def hashstr(string):
    """
    hash加密字符串
    :param string:
    :return:
    """
    md5str = hashlib.md5()
    md5str.update(string)
    result = md5str.hexdigest()
    return result


def phoneValid(phone):
    """
    当用户提交手机号，验证手机号是否注册，如果有，返回用户信息
    :param string:
    :return:
    """
    try:
        u = Users.objects.get(phone=phone)
    except:
        result = {'status': True, 'data': None}
    else:
        result = {'status': False, 'data': u}
    finally:
        return result


def register_phone(request):
    """
    配合ajax，在前端register页面上验证注册手机号码是否重复
    :param request:
    :return:
    """
    if request.method == 'GET' and request.GET:
        phone = request.GET['phone']
        valid = phoneValid(phone)
        if valid['status']:
            result = {'status': 'success'}
        else:
            result = {'status': 'error'}
    else:
        result = {'status': 'phone is not found'}
    return JsonResponse(result)

@loginValid
def register(request):
    """
    注册用户
    :param request:
    :return:
    """
    userid = request.COOKIES.get('user_id')
    try:
        user = Users.objects.get(id=userid)
    except:
        return HttpResponseRedirect('/login/')
    if request.method == 'POST' and request.POST:
        img = request.FILES
        data = request.POST
        photo = img['photo']
        photo_name = str(photo)
        img = Image.open(photo)
        img.save('static/img/uploadImg/'+photo_name)

        u = Users()
        u.phone = data['phone']
        u.user = data['user']
        u.password = hashstr(data['password'])
        u.email = data['email']
        u.birthday = data['birthday']
        u.groups = data['groups']
        u.isadmin = data['isadmin']
        u.photo = photo_name
        try:
            u.save()
            return render_to_response('register_success.html', locals())
        except:
            return render_to_response('register_error.html', locals())

    form = AdminUserForm()
    return render(request, 'register.html', locals())

@loginValid
def userlist(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'GET':
        userList = Users.objects.all()
    return render_to_response('userlist.html', locals())

@loginValid
def modifyuser(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'GET':
        userList = Users.objects.all()
    return render_to_response('modifyuser.html', locals())


@csrf_exempt
def modifyinput(request):
    status = {'status': 'error', 'data': 'no thing need to modify'}
    if request.method == 'POST' and request.POST:
        userid = request.POST['id']
        user = Users.objects.get(id=int(userid))
        print request.POST
        m_username = request.POST['modify_name']
        m_passwd = request.POST['modify_passwd']
        m_phone = request.POST['modify_phone']
        m_email = request.POST['modify_email']
        m_birthday = request.POST['modify_birthday']
        m_groups = request.POST['modify_groups']
        m_isadmin = request.POST['modify_isadmin']
        # modifyinfo = {'user':m_username,'password:'m_passwd,'phone':m_phone,'email':m_email,'birthday':m_birthday,'groups':m_groups,'isadmin':m_isadmin}
        if m_username:
            Users.objects.filter(id=userid).update(user=m_username)
        if m_passwd:
            passwd = hashstr(str(m_passwd))
            Users.objects.filter(id=userid).update(password=passwd)
        if m_phone:
            Users.objects.filter(id=userid).update(phone=m_phone)
        if m_email:
            Users.objects.filter(id=userid).update(email=m_email)
        if m_birthday:
            Users.objects.filter(id=userid).update(birthday=m_birthday)
        if m_groups:
            Users.objects.filter(id=userid).update(groups=m_groups)
        if m_isadmin:
            Users.objects.filter(id=userid).update(isadmin=m_isadmin)

    return JsonResponse(status)