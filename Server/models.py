# coding:utf-8
from django.db import models
from django.views.decorators.csrf import csrf_exempt


# Create your models here.
#@csrf_exempt
class Servers(models.Model):
    hostname = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)
    mac = models.CharField(max_length=32)
    sys = models.CharField(max_length=32)
    cpu = models.CharField(max_length=32)
    memory = models.CharField(max_length=32)
    disk = models.CharField(max_length=32)


class Uploads(models.Model):
    ip = models.CharField(max_length=32)
