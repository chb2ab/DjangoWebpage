# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_auto_20151128_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='lon',
            field=models.FloatField(default=0),
        ),
    ]
