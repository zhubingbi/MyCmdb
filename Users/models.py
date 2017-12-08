# coding=utf-8
from django.db import models

# Create your models here.


class Users(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')

    groups = models.CharField(max_length=32, verbose_name='所属组')
    password = models.CharField(max_length=32, verbose_name='用户密码')
    phone = models.CharField(max_length=32, verbose_name='注册电话')
    birthday = models.CharField(max_length=32, verbose_name='用户生日')
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')

    photo = models.ImageField(upload_to='uploadImg', blank=True, null=True, verbose_name='用户头像')
    isadmin = models.CharField(max_length=32, blank=True, null=True, verbose_name='是否具有管理员权限')

    class Meta:
        db_table = 'Users'
        verbose_name = '用户表'

    def __str__(self):
        return self.user


class Groups(models.Model):
    groupname = models.CharField(max_length=32, verbose_name='用户组名')
    authority = models.CharField(max_length=32, verbose_name='权限')


class Authority(models.Model):
    authcontent = models.CharField(max_length=128, verbose_name='权限内容')
