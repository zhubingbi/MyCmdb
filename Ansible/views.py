# coding:utf-8
import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from Server.models import Servers
from Users.models import Users
from .models import toolscript
from .forms import ToolForm
from django.http import HttpResponse
import json
#from  ansible_runner.runner import AdHocRunner, PlayBookRunner
#from  ansible_runner.runner import CommandResultCallback

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
            return render(request, 'tools/addtools.html', locals())
    else:
        form = ToolForm()
    return render(request, 'tools/addtools.html', locals())


def toolscripts(request):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    serverList = Servers.objects.all()
    return render_to_response('tools/tools-script.html', locals())


def tools_script_get(request, shid):
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'GET':
        obj = Servers.objects.all()
        sh = toolscript.objects.get(id=shid)
        return render(request, 'tools/tools-script.html', locals())


def tools_script_execute(request):
    ret = {'status': 'error', 'data': None, 'msg': None}
    if request.method == 'POST' and request.POST:
        try:
            host_ids = request.POST.getlist('id', None)
            shid = request.POST.get('shid', None)
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
                return HttpResponse(json.dumps(ret))
        except Exception as e:
            ret = {'status': 'error', 'data': None, 'msg': '传输错误{}'.format(e)}
            return HttpResponse(json.dumps(ret))




    return HttpResponse(json.dumps(ret))
