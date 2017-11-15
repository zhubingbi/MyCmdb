# coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import Servers
from django.views.decorators.csrf import csrf_exempt
from MyCmdb.views import loginValid
from Users.models import Users
import paramiko


@csrf_exempt   # 接口避免CSRFtoken验证
def saveServer(request):
    """
    接口提交服务器信息
    :param request:
    :return:
    """
    result = {'status': '', 'data': ''}
    if request.method == 'POST' and request.POST:
        try:
            mac = request.POST['mac']
            server = Servers.objects.get(mac=mac)
        except:
            # 如果是新mac地址，添加新的.
            server = Servers()
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.mac = request.POST['mac']
            server.sys = request.POST['sys']
            server.memory = request.POST['memory']
            server.disk = request.POST['disk']
            server.cpu = request.POST['cpu']
        else:
            # 存在mac地址，就修改原有的.
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.sys = request.POST['sys']
            server.memory = request.POST['memory']
            server.disk = request.POST['disk']
            server.cpu = request.POST['cpu']
        finally:
            server.save()
        result['status'] = 'success'
        result['data'] = 'save success'
    else:
        result['status'] = 'error'
        result['data'] = 'method must be post and not null'
    return JsonResponse(result)


@loginValid
def serverlist(request, number=5):
    number = int(number)
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'GET' and request.GET:
        p = int(request.GET['page'])
    else:
        p = 1
    page_up = (p-1)*number
    page_down = p*number
    all_server = Servers.objects.all()

    serverList = all_server[page_up:page_down]
    total = len(all_server)
    page = total/float(number)
    if int(page) != page:
        page = int(page) + 1
    else:
        page = int(page)
    page_size = range(1, page+1)
    return render(request, 'serverlist.html', locals())


shell_dict = {}  # 设置一个字典用来存储链接


@loginValid
def serverConnect(request):
    status = {'status': 'error', 'data': 'not post '}
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        server_id = request.POST['id']
        ip = Servers.objects.get(id=int(server_id)).ip
        getParmiko(ip, username, password)
        status['status'] = 'success'
        status['data'] = [server_id, ip]
    return JsonResponse(status)


def getParmiko(host, user, password, port=22):
    trans = paramiko.Transport(host, port)
    trans.connect(username=user, password=password)
    shell_dict[host] = {'connection': trans}
    # {"127.0.0.1":{'connection':connect}}
    # 连接的ip, connection索引名  connect函数
    return trans


def exec_cmd(request):
    status = {'status': 'error', 'data': 'Not Found'}
    if request.method == 'GET' and request.GET:
        cmd = request.GET['cmd']
        if '192.168.22.122' in shell_dict:  # 查看当前IP是否有shell 开启
            shell = shell_dict['192.168.22.108']  # 如有就使用
        else:
            trans = getParmiko('192.168.22.108', 'root', 'careland')
            ssh = paramiko.SSHClient()
            ssh._transport = trans

            shell = ssh.invoke_shell()    # 没有就创建，并且添加到字典中
            shell.settimeout(1)
            shell_dict['192.168.22.108'] = shell
        shell.send(cmd+'\n')
        result = ""
        while True:
            try:
                result += shell.recv(9999)
            except:
                break
        status['status'] = 'success'
        status['data'] = result.split('\n')
    return JsonResponse(status)


def doCommand(request):
    status = {'status':'error', 'data':'request mehod must get and not null'}
    if request.method == 'GET' and request.GET:
        ip = request.GET['serverip']
        cmd = request.GET['servercmd']
        data = shell_dict.get(ip)
        # shell_dict {'127.0.0.1': {'connection':connect}}
        # data {"connection":connect}
        # 或者 data {"connection":connect, 'shell':shell}
        if data:
            shell = data.get('shell')   # 有链接的情况下是否有shell
            if not shell:
                # 如果shell 不存在的情况下
                trans = data.get('connection')
                ssh = paramiko.SSHClient()
                ssh._transport = trans
                shell = ssh.invoke_shell()
                shell.settimeout(1)
                shell_dict[ip]['shell'] = shell

            shell.send(cmd+'\n')
            result = ""
            while True:
                try:
                    result += str(shell.recv(99999))
                except:
                    break
            status['status'] = 'success'
            status['data'] = result.replace('\r', '').split('\n')
    return JsonResponse(status)


#def exec_cmd(request):
    #status = {'status': 'error', 'data': 'Not Found'}
    #if request.method == 'GET' and request.GET:
    #    cmd = request.GET['cmd']

#        trans = getParmiko('192.168.22.122', 'root', 'careland')
#        ssh = paramiko.SSHClient()
#        ssh._transport = trans
#        stdin, stdout, stderr = ssh.exec_command(cmd)
#        trans.close()
#        result = stdout.read()
#        status['status'] = 'success'
#        status['data'] = result.split('\n')
#    return JsonResponse(status)

def probeserver(request):
    """
    页面触发刷新
    :param request:
    :return:
    """


def gateone(request):

    return render_to_response('gateone.html', locals())


def upload(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    return render_to_response('upload.html', locals())
