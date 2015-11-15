# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0008_auto_20151103_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
