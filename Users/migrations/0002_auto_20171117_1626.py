# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='birthday',
            field=models.CharField(default=123514, max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x94\x9f\xe6\x97\xa5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.CharField(max_length=32, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x88\x86\xe7\xbb\x84'),
        ),
        migrations.AlterField(
            model_name='users',
            name='isadmin',
            field=models.CharField(max_length=32, null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x85\xb7\xe6\x9c\x89\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98\xe6\x9d\x83\xe9\x99\x90', blank=True),
        ),
    ]
