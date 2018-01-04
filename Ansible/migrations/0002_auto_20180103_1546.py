# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ansible', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url', models.CharField(max_length=255, verbose_name=b'URL\xe5\x90\x8d\xe7\xa7\xb0')),
                ('argument_list', models.CharField(help_text=b'\xe5\xa4\x9a\xe4\xb8\xaa\xe5\x8f\x82\xe6\x95\xb0\xe4\xb9\x8b\xe9\x97\xb4\xe7\x94\xa8\xe8\x8b\xb1\xe6\x96\x87\xe5\x8d\x8a\xe8\xa7\x92\xe9\x80\x97\xe5\x8f\xb7\xe9\x9a\x94\xe5\xbc\x80', max_length=255, null=True, verbose_name=b'\xe5\x8f\x82\xe6\x95\xb0\xe5\x88\x97\xe8\xa1\xa8', blank=True)),
                ('describe', models.CharField(max_length=255, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'verbose_name': 'ansible\u6743\u9650\u8868',
                'verbose_name_plural': 'ansible\u6743\u9650\u8868',
                'permissions': (('addtool', '\u6dfb\u52a0\u5de5\u5177'), ('deltool', '\u5220\u9664\u5de5\u5177'), ('deltools', '\u6279\u91cf\u5220\u9664\u5de5\u5177'), ('updatetool', '\u66f4\u65b0\u5de5\u5177'), ('dotool', '\u6267\u884c\u5de5\u5177')),
            },
        ),
        migrations.AlterModelOptions(
            name='toolscript',
            options={'verbose_name': '\u811a\u672c\u5de5\u5177\u8868', 'verbose_name_plural': '\u811a\u672c\u5de5\u5177\u8868'},
        ),
    ]
