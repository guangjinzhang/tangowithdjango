# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MyStreet', '0002_auto_20150322_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='average_business_rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='street',
            name='average_infrastructure_rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='street',
            name='average_rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='street',
            name='average_safety_rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 20, 37, 36, 982000), null=True),
            preserve_default=True,
        ),
    ]
