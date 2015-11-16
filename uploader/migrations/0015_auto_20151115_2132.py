# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0014_auto_20151115_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
