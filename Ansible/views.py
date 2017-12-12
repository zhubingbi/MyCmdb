# coding:utf-8
import os
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from Server.models import Servers
from Users.models import Users
from .models import toolscript
from .forms import ToolForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from Platform.models import Toollog
import json
#from  ansible_runner.runner import AdHocRunner, PlayBookRunner
#from  ansible_runner.runner import CommandResultCallback

# Create your views here.


# def hostlist(request):
#     """
#     显示所有服务器列表，在执行工具页面展示勾选服务器
#     :param request:
#     :return:
#     """
#     userid = request.COOKIES.get('user_id')
#     user = Users.objects.get(id=userid)
#     serverList = Servers.objects.all()
#     return render_to_response('hostlist.html', locals())


def tools(request):
    """
    展示所有的工具列表
    :param request:
    :return:
    """
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    obj = toolscript.objects.all()
    return render_to_response('tools/tools.html', locals())


def addtools(request):
    """
    添加工具
    :param request:
    :return:
    """
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'POST' and request.POST:
        form = ToolForm(request.POST)
        if form.is_valid():
            tools_save = form.save()
            form = ToolForm()
            return render(request, 'tools/addtools.html', locals())
    else:
        form = ToolForm()
    return render(request, 'tools/addtools.html', locals())


# def toolscripts(request):
#     userid = request.COOKIES.get('user_id')
#     user = Users.objects.get(id=userid)
#     serverList = Servers.objects.all()
#     return render_to_response('tools/tools-script.html', locals())


def tools_script_get(request, shid):
    """
    选中获取工具
    :param request:
    :param shid:
    :return:
    """
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'GET':
        obj = Servers.objects.all()
        sh = toolscript.objects.get(id=shid)
        return render(request, 'tools/tools-script.html', locals())


def tools_script_execute(request):
    """
    获取工具内容，获取选中服务器IP，执行
    :param request:
    :return:
    """
    ret = {'status': 'error', 'data': None, 'msg': None}
    if request.method == 'POST' and request.POST:
        try:
            host_ids = request.POST.getlist('id', None)
            # host_ids 里面包含了所有前端传递过来的选中的ip 服务器
            shid = request.POST.get('shid', None)
            # shid 是tool工具的id值

            if not host_ids:
                ret = {'status': 'False', 'data': None, 'msg': '请选择主机'}
                return HttpResponse(json.dumps(ret))
            ips = []
            for i in host_ids:
                s = Servers.objects.get(id=i)
                ip = s.ip
                ips.append(ip)
            ipstring = ','.join(ips)
            sh = toolscript.objects.filter(id=shid)

            for item in sh:
                if item.tooltype == 0:
                    with open('Ansible/script/test.sh', 'w+') as f:
                        f.write(item.toolscript)
                        a = 'Ansible/script/{}.sh'.format(item.id)
                    os.system("sed 's/\r//' Ansible/script/test.sh > {}".format(a))

                elif item.tooltype == 1:
                    with open('Ansible/script/test.py', 'w+') as f:
                        f.write(item.toolscript)
                        a = 'Ansible/script/{}.py'.format(item.id)
                    os.system("sed 's/\r//' Ansible/script/test.py > {}".format(a))

                elif item.tooltype == 2:
                    with open('Ansible/script/test.yml', 'w+') as f:
                        f.write(item.toolscript)
                        a = 'Ansible/script/{}.yml'.format(item.id)
                    os.system("sed 's/\r//' Ansible/script/test.yml > {}".format(a))
                else:
                    ret = {'status': 'False', 'data': None, 'msg': '脚本类型错误,只能是shell, python, yml格式'}
                    return HttpResponse(json.dumps(ret))

                data1 = []
                for hostid in host_ids:
                    try:
                        serverinfo = Servers.objects.get(id=hostid)
                        data2 = {}
                        info = [
                            {
                                "hostname": serverinfo.hostname,
                                "ip": serverinfo.ip,
                                "port": '22',
                                "username": 'root',
                                "password": 'careland',
                            },
                        ]

                        if item.tooltype == 0:
                            ansible_tuple = (('script', a),)
                            hoc = AdHocRunner(hosts=info)
                            hoc.results_callback = CommandResultCallback()
                            r = hoc.run(ansible_tuple)
                            data2[ip] = serverinfo.ip
                            data2['data'] = r['contacted'][serverinfo.hostname]['stdout']
                            data1.append(data2)

                        elif item.tooltype == 1:
                            ansible_tuple = (('script', a),)
                            hoc = AdHocRunner(hosts=info)
                            hoc.results_callback = CommandResultCallback()
                            r = hoc.run(ansible_tuple)
                            data2['ip'] = serverinfo.ip
                            data2['data'] = r['contacted'][serverinfo.hostname]['stdout']
                            data1.append(data2)

                        elif item.tooltype == 2:
                            play = PlayBookRunner(info, playbook_path=a)
                            b = play.run()
                            data2['ip'] = serverinfo.ip
                            data2['data'] = b['plays'][0]['tasks'][1]['hosts'][h.hostname]['stdout'] + \
                                                b['plays'][0]['tasks'][1]['hosts'][h.hostname]['stderr']
                            data1.append(data2)
                        else:
                            data2['ip'] = '脚本类型错误'
                            data2['data'] = '脚本类型错误'
                    except Exception as e:
                         data2['ip'] = serverinfo.ip
                         data2['data'] = '远程执行权限限制，请修改{}'.format(e)
                         data1.append(data2)

                ret = {'data': data1}

                userid = request.COOKIES.get('user_id')
                user = Users.objects.get(id=userid)
                tool = toolscript.objects.get(id=shid)
                username = user.user
                serverip = ipstring
                toolname = tool.toolname
                toolcontent = tool.toolscript
                login_ip = request.META['REMOTE_ADDR']
                Toollog.objects.create(user=username, server_ip=serverip, tool_name=toolname, tool_content=toolcontent, ip=login_ip)
                # 执行成功的时候，记录日志
                return HttpResponse(json.dumps(ret))
        except Exception as e:
            ret = {'status': 'error', 'data': None, 'msg': '传输错误{}'.format(e)}
            return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


@csrf_exempt
def tool_delete(request):
    """
    删除工具
    :param request:
    :return:
    """
    ret = {'status': 'error', 'msg': '请求参数为空'}
    if request.method == 'POST' and request.POST:
        try:
            shid = request.POST.get('nid')
            toolscript.objects.get(id=shid).delete()
        except Exception as e:
            ret['status'] = False
            ret['error'] = '删除请求错误，{}'.format(e)
    return HttpResponse(json.dumps(ret))


@csrf_exempt
def tools_delete(request):
    """
    批量删除工具
    :param request:
    :return:
    """
    ret = {'status':'error', 'msg':'请求参数为空'}
    if request.method == 'POST' and request.POST:
        try:
            shids = request.POST.getlist('id')
            idstring = ','.join(shids)
            toolscript.objects.extra(where=['id IN (' + idstring + ')']).delete()
        except Exception as e:
            ret['status'] = 'error'
            ret['msg'] = '删除请求错误，{}'.format(e)
    return HttpResponse(json.dumps(ret))


@csrf_exempt
def tool_update(request, shid):
    """
    更新工具
    :param request:
    :param shid:所选的脚本ID值
    :return:
    """
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    tool_id = toolscript.objects.get(id=shid)
    id = shid
    if request.method == 'POST' and request.POST:
        form = ToolForm(request.POST, instance=tool_id)
        if form.is_valid():
            asset_save = form.save()
            return HttpResponseRedirect('/ansible/tools')
    form = ToolForm(instance=tool_id)
    return render(request, 'tools/tool-update.html', locals())

