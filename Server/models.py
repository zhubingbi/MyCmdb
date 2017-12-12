# coding:utf-8
from django.db import models
import django.utils.timezone as timezone
from django.views.decorators.csrf import csrf_exempt


class Servers(models.Model):
    hostname = models.CharField(max_length=128, verbose_name='主机名', blank=True, null=True)
    ip = models.CharField(max_length=128, verbose_name='ip', blank=True, null=True)
    mac = models.CharField(max_length=128, verbose_name='mac地址', blank=True, null=True)
    sys = models.CharField(max_length=128, verbose_name='系统版本', blank=True, null=True)
    cpu = models.CharField(max_length=128, verbose_name='cpu', blank=True, null=True)
    memory_total = models.CharField(max_length=128, verbose_name='内存总量', blank=True, null=True)
    memory_cached = models.CharField(max_length=128, verbose_name='cached值', blank=True, null=True)
    memory_buffers = models.CharField(max_length=128, verbose_name='buffer值', blank=True, null=True)
    memory_free = models.CharField(max_length=128, verbose_name='内存剩余', blank=True, null=True)
    disk_total = models.CharField(max_length=128, verbose_name='磁盘总量', blank=True, null=True)
    disk_free = models.CharField(max_length=128, verbose_name='磁盘剩余空间', blank=True, null=True)

    on_line = models.CharField(max_length=64, blank=True, null=True, verbose_name='服务器所属产品线')
    active = models.CharField(max_length=32, blank=True, null=True, verbose_name='服务器是否存活？ 1为是，0为否')
    port = models.CharField(max_length=32, default='22', verbose_name='ssh端口', blank=True, null=True)

    content = models.TextField(blank=True, null=True, verbose_name='备注信息')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建日期', blank=True, null=True)
    utime = models.DateTimeField(auto_now=True, verbose_name='最后修改日期', blank=True, null=True)


    class Meta:
        db_table = 'Servers'
        verbose_name = '服务器详情'

    def __str__(self):
        return self.ip


class Servers_info(models.Model):
    ip = models.CharField(max_length=128, verbose_name='服务器IP地址')
    cpu_info = models.CharField(max_length=128, verbose_name='CPU负载')
    memory_info = models.CharField(max_length=128, verbose_name='内存百分比')
    disk_info = models.CharField(max_length=128, verbose_name='磁盘百分比')
    utime = models.DateTimeField(auto_now=True, verbose_name='最后修改日期')

    class Meta:
        db_table = 'Servers_info'
        verbose_name = '服务器状况表'

    def __str__(self):
        return self.ip
