# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MyStreet', '0005_auto_20150323_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 0, 19, 11, 613000), null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='street',
            name='image',
            field=models.ImageField(upload_to=b'/images', blank=True),
            preserve_default=True,
        ),
    ]
