# coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import Servers, ServerStatus
from django.views.decorators.csrf import csrf_exempt
from MyCmdb.views import loginValid
from Users.models import UserProfile
from forms import ServersForm
import paramiko
from permission import check_permission
from Interface.models import Interface_sys
from Platform.models import Serverlog
import time, datetime
from pyecharts import Gauge, Line
from django.template import loader
import json


@csrf_exempt   # 接口避免CSRFtoken验证
def saveserver(request):
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
            server.memory_total = request.POST['memory_total']
            server.memory_free = request.POST['memory_free']
            server.memory_cached = request.POST['memory_cached']
            server.memory_buffers = request.POST['memory_buffers']
            server.disk_total = request.POST['disk_total']
            server.disk_free = request.POST['disk_free']
            server.cpu = request.POST['cpu']
        else:
            # 存在mac地址，就修改原有的.
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.sys = request.POST['sys']
            server.memory_total = request.POST['memory_total']
            server.memory_free = request.POST['memory_free']
            server.memory_cached = request.POST['memory_cached']
            server.memory_buffers = request.POST['memory_buffers']
            server.disk_total = request.POST['disk_total']
            server.disk_free = request.POST['disk_free']
            server.cpu = request.POST['cpu']
        finally:
            server.save()
        result['status'] = 'success'
        result['data'] = 'save success'
    else:
        result['status'] = 'error'
        result['data'] = 'method must be post and not null'
    return JsonResponse(result)


# @loginValid
# def serverlist(request, number=5):
#     number = int(number)
#     userid = request.COOKIES.get('user_id')
#     user = Users.objects.get(id=userid)
#     if request.method == 'GET' and request.GET:
#         p = int(request.GET['page'])
#     else:
#         p = 1
#     page_up = (p-1)*number
#     page_down = p*number
#     all_server = Servers.objects.all()
#
#     serverList = all_server[page_up:page_down]
#     total = len(all_server)
#     page = total/float(number)
#     if int(page) != page:
#         page = int(page) + 1
#     else:
#         page = int(page)
#     page_size = range(1, page+1)
#     return render(request, 'server/serverlist.html', locals())


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
    userid = request.COOKIES.get('user_id')
    user = UserProfile.objects.get(id=userid)
    status = {'status': 'error', 'data': 'request method must get and not null'}
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
            login_ip = request.META['REMOTE_ADDR']
            Serverlog.objects.create(user=user.user, ip=login_ip, server_ip=ip, cmd=cmd)
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

def gateone(request):
    return render_to_response('server/gateone.html', locals())


@loginValid
def serverlist(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    server_list = Servers.objects.all()
    serverlist_active = 'active'
    server_isactive = 'active'
    return render(request, 'server/testlist.html', locals())

@loginValid
def serverinfo(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    serverid = int(request.GET.get("serverid"))
    #serverid = int(serverid)
    server_info = Servers.objects.get(id=serverid)
    serverlist_active = 'active'
    server_isactive = 'active'
    return render_to_response('server/testinfo.html', locals())


@csrf_exempt
@check_permission
def serverupdate(request):
    userid = request.COOKIES.get('user_id')
    try:
        user = UserProfile.objects.get(id=userid)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/login')
    serverid = int(request.GET.get('serverid'))
    serverinfo = Servers.objects.get(id=serverid)
    if request.method == 'POST':
        form = ServersForm(request.POST, instance=serverinfo)
        server_save = form.save()
        url = '/server/serverinfo/?serverid='+str(serverid)
        return HttpResponseRedirect(url)
    form = ServersForm(instance=serverinfo)
    serverlist_active = 'active'
    server_isactive = 'active'
    return render(request, 'server/testupdate.html', locals())


def Gauge_cpumem(attr, data):
    bar = Gauge("", width=600, height=300)
    bar.add("", attr, data)
    return bar


def Line_network(d, title, title1, date, network_in, network_put):
    bar = Line(d, width=1600, height=500)
    bar.add(title, date, network_in)
    bar.add(title1, date, network_put)
    return bar

def pyecharts_add(echa):
    """
    echarts 添加 自适应 宽度
    :param echa:
    :return:
    """
    a = echa.split('</div>')
    a1 = a[0].split('"')
    b = a1[3].split(';')
    a1[3] = b[1]
    div = '"'.join(a1)

    onresize = "    myChart_%s.resize(); " % (a1[1])
    ret = div + "</div>" + a[1]
    return ret, onresize


def serverstatus(request):
    try:
        userid = request.COOKIES.get('user_id')
        try:
            user = UserProfile.objects.get(id=userid)
        except UserProfile.DoesNotExist:
            return HttpResponseRedirect('/login')
        serverid = int(request.GET.get('serverid'))
        all = ServerStatus.objects.all()
        template = loader.get_template('server/serversys.html')
        now = datetime.datetime.now()
        last_time = now+datetime.timedelta(days=-7)
        date, cpu_use, mem_use, in_net, out_net = [], [], [], [], []
        serverlist_active = 'active'
        server_isactive = 'active'
        for i in all:
            if i.server_id == int(serverid):
                date.append(i.ctime.strftime("%m-%d %H:%M"))
                cpu_use.append(i.cpu_use)
                mem_use.append(i.mem_use)
                in_net.append(i.in_net)
                out_net.append(i.out_net)
            if cpu_use:
                cpu_data = cpu_use[-1]
                mem_data = mem_use[-1]
            else:
                cpu_data = 0
                mem_data = 0

            cpu = Gauge_cpumem(attr="CPU", data=cpu_data)
            mem = Gauge_cpumem(attr="内存", data=mem_data)
            network = Line_network(d="kb/s", title="进流量", title1="出流量", date=date, network_in=in_net,
                                   network_put=out_net)
            history_cpumem = Line_network(d="%", title="CPU", title1="内存", date=date, network_in=cpu_use,
                                          network_put=mem_use)
            context = dict(
                cpu=pyecharts_add(cpu.render_embed())[0],
                mem=pyecharts_add(mem.render_embed())[0],
                network=pyecharts_add(network.render_embed())[0],
                history_cpumem=pyecharts_add(history_cpumem.render_embed())[0],
                script_list=cpu.get_js_dependencies(),
                serverlist_active='active',
                server_isactive = 'active',
                user = user,
                onresize=" <script>  window.onresize = function () {  %s %s  %s  %s };  </script>" % (
                pyecharts_add(cpu.render_embed())[1], pyecharts_add(mem.render_embed())[1],
                pyecharts_add(network.render_embed())[1], pyecharts_add(history_cpumem.render_embed())[1],)
            )
            return HttpResponse(template.render(context, request))
    except Exception as e:
        error = "错误,{}".format(e)
        server_list = Servers.objects.all()
        return render(request, 'server/testlist.html', locals())

