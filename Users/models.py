# coding=utf-8
from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='用户密码')
    phone = models.CharField(max_length=32, verbose_name='注册电话')
    birthday = models.CharField(max_length=32, verbose_name='用户生日')
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')
    groups = models.CharField(max_length=32, null=True, verbose_name='用户业务分组')
    photo = models.ImageField(upload_to='uploadImg', blank=True, null=True, verbose_name='用户头像')
    isadmin = models.CharField(max_length=32, blank=True, null=True, verbose_name='是否具有管理员权限')