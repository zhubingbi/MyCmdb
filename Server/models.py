# coding:utf-8
from django.db import models
from django.views.decorators.csrf import csrf_exempt


class Servers(models.Model):
    hostname = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    mac = models.CharField(max_length=128)
    sys = models.CharField(max_length=128)
    cpu = models.CharField(max_length=128)
    memory_total = models.CharField(max_length=128)
    memory_cached = models.CharField(max_length=128)
    memory_buffers = models.CharField(max_length=128)
    memory_free = models.CharField(max_length=128)
    disk_total = models.CharField(max_length=128)
    disk_free = models.CharField(max_length=128)
    on_line = models.CharField(max_length=64, blank=True, null=True, verbose_name='服务器所属产品线')
