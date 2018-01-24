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

    active = models.BooleanField(default=True, verbose_name='是否启用')
    port = models.CharField(max_length=32, default='22', verbose_name='ssh端口', blank=True, null=True)

    content = models.TextField(blank=True, null=True, verbose_name='备注信息')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建日期', blank=True, null=True)
    utime = models.DateTimeField(auto_now=True, verbose_name='最后修改日期', blank=True, null=True)

    class Meta:
        db_table = 'Servers'
        verbose_name = '服务器信息详情'
        verbose_name_plural = '服务器信息详情'

    def __str__(self):
        return self.ip


class ServerStatus(models.Model):
    cpu_use = models.CharField(verbose_name='cpu使用率', null=True, blank=True, max_length=32)
    mem_use = models.CharField(verbose_name='内存使用率', null=True, blank=True, max_length=32)
    in_net = models.CharField(verbose_name='入口流量', null=True, blank=True, max_length=32)
    out_net = models.CharField(verbose_name='出口流量', null=True, blank=True, max_length=32)
    server = models.ForeignKey(Servers, on_delete=models.CASCADE,)

    cdate = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    udate = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'ServerStatus'
        verbose_name = '服务器性能监控表'
        verbose_name_plural = verbose_name
        ordering = ['udate']

    def __str__(self):
        return self.cpu_use


class Permission(models.Model):
    name = models.CharField("权限名称", max_length=64)
    url = models.CharField('URL名称', max_length=255)
    argument_list = models.CharField('参数列表', max_length=255, help_text='多个参数之间用英文半角逗号隔开', blank=True, null=True)
    describe = models.CharField('描述', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
        # 权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
        permissions = (
            ('update_server', '更新具体服务器信息表'),
        )
