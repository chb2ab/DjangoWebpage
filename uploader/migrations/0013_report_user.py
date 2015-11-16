# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0012_auto_20151105_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.CharField(default='x', max_length=50),
        ),
    ]
