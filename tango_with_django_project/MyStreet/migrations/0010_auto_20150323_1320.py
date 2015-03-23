# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MyStreet', '0009_auto_20150323_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 13, 20, 55, 551000), null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='street',
            name='image',
            field=models.ImageField(upload_to=b'image', blank=True),
            preserve_default=True,
        ),
    ]
