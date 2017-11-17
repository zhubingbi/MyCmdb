# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='toolscript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('toolname', models.CharField(unique=True, max_length=255, verbose_name=b'\xe5\xb7\xa5\xe5\x85\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('toolscript', models.TextField(null=True, verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac', blank=True)),
                ('tooltype', models.IntegerField(default=0, verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'shell'), (1, b'python'), (2, b'yml')])),
                ('comment', models.TextField(null=True, verbose_name=b'\xe5\xb7\xa5\xe5\x85\xb7\xe8\xaf\xb4\xe6\x98\x8e', blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
