# coding=utf-8
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    groups = models.ForeignKey(to=Group, to_field='id', on_delete=models.SET_NULL, verbose_name='业务组',null=True)
    phone = models.CharField(max_length=32, verbose_name='注册电话')
    photo = models.ImageField(upload_to='uploadImg', blank=True, null=True, verbose_name='用户头像')
    birthday = models.CharField(max_length=32, verbose_name='用户生日')
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')

    class Meta:
        db_table = 'UserProfile'
        verbose_name = '平台用户表'
        verbose_name_plural = verbose_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)

