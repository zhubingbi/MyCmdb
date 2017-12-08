# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20171206_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '\u7528\u6237\u8868'},
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
    ]
