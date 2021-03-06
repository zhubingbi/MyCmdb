# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loginlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=32, null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'Loginlog',
                'verbose_name': '\u5e73\u53f0\u767b\u5f55\u65e5\u5fd7\u5386\u53f2\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Serverlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=32, null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7\xe6\x9d\xa5\xe6\xba\x90IP')),
                ('server_ip', models.CharField(max_length=32, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP')),
                ('cmd', models.CharField(max_length=32, null=True, verbose_name=b'\xe8\xbe\x93\xe5\x85\xa5\xe5\x91\xbd\xe4\xbb\xa4\xe6\x93\x8d\xe4\xbd\x9c')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'Serverlog',
                'verbose_name': '\u767b\u5f55\u670d\u52a1\u5668\u5386\u53f2\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Toollog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=32, null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7')),
                ('server_ip', models.CharField(max_length=32, null=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('tool_name', models.CharField(max_length=32, null=True, verbose_name=b'\xe5\xb7\xa5\xe5\x85\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('tool_content', models.TextField(null=True, verbose_name=b'\xe5\xb7\xa5\xe5\x85\xb7\xe5\x86\x85\xe5\xae\xb9')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7\xe6\x9d\xa5\xe6\xba\x90IP')),
            ],
            options={
                'db_table': 'Toollog',
                'verbose_name': '\u5de5\u5177\u6267\u884c\u5386\u53f2\u8bb0\u5f55',
            },
        ),
    ]
