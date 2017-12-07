# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20171117_1626'),
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
                ('exprie', models.CharField(max_length=64, verbose_name=b'\xe7\xbb\x84\xe8\xaf\xb4\xe6\x98\x8e')),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='isadmin',
        ),
        migrations.AlterField(
            model_name='users',
            name='groups',
            field=models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xbb\x84'),
        ),
    ]
