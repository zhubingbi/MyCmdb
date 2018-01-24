# coding=utf-8
from django.db import models
from Server.models import Servers


class Interface_status(models.Model):
    interface_name = models.CharField(max_length=128, verbose_name='接口/服务名', blank=True, null=True)
    ip = models.CharField(max_length=128, verbose_name='服务器IP地址', blank=True, null=True)
    interface_status = models.CharField(max_length=64, verbose_name='接口/服务状态', blank=True, null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建日期', blank=True, null=True)
    utime = models.DateTimeField(auto_now=True, verbose_name='更新日期', blank=True, null=True)

    class Meta:
        db_table = 'Interface_status'
        verbose_name = '接口/服务状态表'
        verbose_name_plural = '接口/服务状态表'

    def __str__(self):
        return self.interface_name


class Interface_url(models.Model):
    interface_url = models.CharField(max_length=128, verbose_name='url地址', blank=True, null=True)
    url_result = models.TextField(blank=True, null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建日期', blank=True, null=True)
    utime = models.DateTimeField(auto_now=True, verbose_name='更新日期', blank=True, null=True)

    class Meta:
        db_table = "Interface_url"
        verbose_name = '服务-监控项表'
        verbose_name_plural = '服务-监控项表'

    def __str__(self):
        return self.interface_url


class Interface_sys(models.Model):
    cpu_use = models.CharField(verbose_name='cpu使用率', null=True, blank=True, max_length=32)
    mem_use = models.CharField(verbose_name='内存使用率', null=True, blank=True, max_length=32)
    in_net = models.CharField(verbose_name='入口流量', null=True, blank=True, max_length=32)
    out_net = models.CharField(verbose_name='出口流量', null=True, blank=True, max_length=32)
    server = models.ForeignKey(Servers, on_delete=models.CASCADE,)

    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'Interface_sys'
        verbose_name = '系统监控状态'
        verbose_name_plural = verbose_name
        ordering = ['ctime']

    def __str__(self):
        return self.cpu_use



