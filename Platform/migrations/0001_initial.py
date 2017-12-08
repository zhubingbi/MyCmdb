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
                'verbose_name': '\u5e73\u53f0\u767b\u5f55\u65e5\u5fd7',
            },
        ),
    ]
