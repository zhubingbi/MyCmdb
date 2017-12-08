# coding=utf-8
from django.db import models

__all__ = ['login_log']


class Loginlog(models.Model):
    user = models.CharField(max_length=32, verbose_name='登录用户', null=True)
    ip = models.GenericIPAddressField(verbose_name='用户地址', null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        db_table = "Loginlog"
        verbose_name = "平台登录日志"

    def __str__(self):
        return self.user


class Server_logs(models.Model):
    user = models.CharField(max_length=32, verbose_name='登录用户', null=True)
    ip = models.GenericIPAddressField(verbose_name='登录用户来源IP', null=True)
    server_ip = models.CharField(max_length=32, verbose_name='登录服务器IP')
    cmd = models.CharField(max_length=32, verbose_name='输入命令操作', null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        db_table = 'Server_logs'
        verbose_name = '登录服务器历史'

    def __str__(self):
        return self.user
