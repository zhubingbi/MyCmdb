# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20171206_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='exprie',
        ),
        migrations.AddField(
            model_name='users',
            name='isadmin',
            field=models.CharField(max_length=32, null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x85\xb7\xe6\x9c\x89\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe6\x9d\x83\xe9\x99\x90', blank=True),
        ),
    ]
