# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MyStreet', '0003_auto_20150322_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 20, 44, 24, 62000), null=True),
            preserve_default=True,
        ),
    ]
