# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=32, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe7\x94\xb5\xe8\xaf\x9d')),
                ('photo', models.ImageField(upload_to=b'uploadImg', null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('birthday', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x94\x9f\xe6\x97\xa5')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe7\xbb\x84', to='auth.Group', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserProfile',
                'verbose_name': '\u5e73\u53f0\u7528\u6237\u8868',
                'verbose_name_plural': '\u5e73\u53f0\u7528\u6237\u8868',
            },
        ),
        migrations.DeleteModel(
            name='Authority',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
