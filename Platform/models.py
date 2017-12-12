# coding=utf-8
from django.db import models

__all__ = ['login_log']


class Loginlog(models.Model):
    user = models.CharField(max_length=32, verbose_name='登录用户', null=True)
    ip = models.GenericIPAddressField(verbose_name='用户地址', null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        db_table = "Loginlog"
        verbose_name = "平台登录日志历史记录"

    def __str__(self):
        return self.user


class Serverlog(models.Model):
    user = models.CharField(max_length=32, verbose_name='登录用户', null=True)
    ip = models.GenericIPAddressField(verbose_name='登录用户来源IP', null=True)
    server_ip = models.CharField(max_length=32, verbose_name='登录服务器IP')
    cmd = models.CharField(max_length=32, verbose_name='输入命令操作', null=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        db_table = 'Serverlog'
        verbose_name = '登录服务器历史记录'

    def __str__(self):
        return self.user


class Toollog(models.Model):
    user = models.CharField(max_length=32, verbose_name='登录用户', null=True)
    server_ip = models.CharField(max_length=32, verbose_name='执行服务器', null=True)
    tool_name = models.CharField(max_length=32, verbose_name='工具名称', null=True)
    tool_content = models.TextField(null=True, verbose_name='工具内容')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='执行时间')
    ip = models.GenericIPAddressField(verbose_name='登录用户来源IP', null=True)

    class Meta:
        db_table = 'Toollog'
        verbose_name = '工具执行历史记录'

    def __str__(self):
        return self.tool_name
