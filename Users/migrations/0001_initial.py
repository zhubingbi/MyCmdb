# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authcontent', models.CharField(max_length=128, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xbb\x84\xe5\x90\x8d')),
                ('authority', models.CharField(max_length=32, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('groups', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xbb\x84')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('phone', models.CharField(max_length=32, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe7\x94\xb5\xe8\xaf\x9d')),
                ('birthday', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x94\x9f\xe6\x97\xa5')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('photo', models.ImageField(upload_to=b'uploadImg', null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('isadmin', models.CharField(max_length=32, null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x85\xb7\xe6\x9c\x89\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe6\x9d\x83\xe9\x99\x90', blank=True)),
            ],
            options={
                'db_table': 'Users',
                'verbose_name': '\u7528\u6237\u8868',
            },
        ),
    ]
