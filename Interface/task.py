# coding=utf-8
import urllib2
import paramiko
from models import *
from celery import task
from Server.models import Servers, ServerStatus
import threading, time, datetime


def ssh(ip, cmd, port=22, username='root', password='careland'):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=int(port), username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(cmd, timeout=10)
        print stdout

        result = stdout.read()
        result_decode = result.decode()
        error = stderr.read().decode('utf-8')

        if not error:
            ret = {"ip":ip, "data":result_decode}
            ssh.close()
            return ret

    except Exception as e:
        error = "无法和目标服务器建立连接, {}".format(e)
        ret = {"ip": ip, "data": error}
        return ret


def job(id):
    server = Servers.objects.filter(id=id).first()
    print server.ip
    cpu1 = ssh(ip=server.ip, cmd="top -bn 1 -i -c | grep Cpu")
    print cpu1
    cpu2 = cpu1['data'].split()
    cpu3 = cpu2[1].split('%')
    cpu4 = cpu2[3].split('%')

    print str(cpu3[0])
    print str(cpu4[0])
    cpu = str(float(str(cpu3[0])) + float(str(cpu4[0])))

    total = ssh(ip=server.ip, cmd="free | grep  Mem:")
    list = total['data'].split(" ")
    while '' in list:
        list.remove('')
    mem = float('%.2f' % (float('%.3f' % (int(list[2]) / int(list[1]))) * 100))

    in1 = ssh(ip=server.ip, cmd="cat /proc/net/dev|grep ens37")
    in2 = in1['data'].split()

    time.sleep(1)
    in3 = ssh(ip=server.ip, cmd="cat /proc/net/dev|grep ens37")
    in4 = in3['data'].split()

    in_network = int((int(in4[1]) - int(in2[1]))/1024/10*8)
    out_network = int((int(in4[9]) - int(in2[9]))/1024/10*8)

    ServerStatus.objects.create(server_id=server.id, cpu_use=cpu, mem_use=mem, in_net=in_network, out_net=out_network)


@task
def monitor_job():
    object = Servers.objects.all()
    server_list = []
    for server in object:
        server_list.append(server.id)
    t_list = []
    for i in server_list:
        t = threading.Thread(target=job, args=[i, ])
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()


def scanserver(ip, interface):
    """
    前端传入需要扫描的port, 返回port信息
    :param ip: str_ip
    :param interface: 服务名称
    :return:
    """
    cmd = "netstat -anp|grep %s|head -1" % str(interface)
    print cmd
    server_status = ssh(ip=ip, cmd=cmd)
    if server_status['data']:
        Interface_status.objects.create(interface_name=interface, ip=ip, interface_status='success')
    else:
        Interface_status.objects.create(interface_name=interface, ip=ip, interface_status='error')


@task
def monitory_scan(ip, interface):
    ip = str(ip).split(',')
    t_list = []
    for i in ip:
        t = threading.Thread(target=scanserver, args=[i, interface,])
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()


@task
def scanurl(url, data=None):
    """
    对输入的url,进行ip遍历扫描
    :param ip:
    :param url:
    :return:
    """
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    }
    data = None
    try:
        request = urllib2.Request(url,data=data,headers=headers)
        response = urllib2.urlopen(request)
        result = response.read()
    except Exception as e:
        error = "访问错误,{}".format(e)
        result = error
    Interface_url.objects.create(interface_url=url, url_result=result)


def sacninterface(name, port=None):



@task
def clean_history_monitory():
    now = datetime.datetime.now()
    last_time = now + datetime.timedelta(days=-7)
    Interface_sys.objects.filter(ctiem__lt=last_time).delete()
    Interface_url.objects.filter(ctime__lt=last_time).delete()





