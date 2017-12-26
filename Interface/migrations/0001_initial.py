# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interface_name', models.CharField(max_length=128, null=True, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3/\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8d', blank=True)),
                ('ip', models.CharField(max_length=128, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('interface_status', models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\xa3/\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f', null=True)),
                ('utime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f', null=True)),
            ],
            options={
                'db_table': 'Interface_status',
                'verbose_name': '\u63a5\u53e3/\u670d\u52a1\u72b6\u6001\u8868',
                'verbose_name_plural': '\u63a5\u53e3/\u670d\u52a1\u72b6\u6001\u8868',
            },
        ),
        migrations.CreateModel(
            name='Interface_sys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpu_use', models.CharField(max_length=32, null=True, verbose_name=b'cpu\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87', blank=True)),
                ('mem_use', models.CharField(max_length=32, null=True, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87', blank=True)),
                ('in_net', models.CharField(max_length=32, null=True, verbose_name=b'\xe5\x85\xa5\xe5\x8f\xa3\xe6\xb5\x81\xe9\x87\x8f', blank=True)),
                ('out_net', models.CharField(max_length=32, null=True, verbose_name=b'\xe5\x87\xba\xe5\x8f\xa3\xe6\xb5\x81\xe9\x87\x8f', blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('server', models.ForeignKey(to='Server.Servers')),
            ],
            options={
                'ordering': ['ctime'],
                'db_table': 'Interface_sys',
                'verbose_name': '\u7cfb\u7edf\u76d1\u63a7\u72b6\u6001',
                'verbose_name_plural': '\u7cfb\u7edf\u76d1\u63a7\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='Interface_url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interface_url', models.CharField(max_length=128, null=True, verbose_name=b'url\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('url_result', models.TextField(null=True, blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f', null=True)),
                ('utime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f', null=True)),
            ],
            options={
                'db_table': 'Interface_url',
                'verbose_name': '\u670d\u52a1-\u76d1\u63a7\u9879\u8868',
                'verbose_name_plural': '\u670d\u52a1-\u76d1\u63a7\u9879\u8868',
            },
        ),
    ]
