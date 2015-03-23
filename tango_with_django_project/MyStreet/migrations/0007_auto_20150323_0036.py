# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MyStreet', '0006_auto_20150323_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 0, 36, 2, 304000), null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='street',
            name='image',
            field=models.ImageField(upload_to=b'/static/images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'/static/images', blank=True),
            preserve_default=True,
        ),
    ]
