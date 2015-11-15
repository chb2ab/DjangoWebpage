# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0006_auto_20151103_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='report',
            field=models.ForeignKey(to='uploader.Report'),
        ),
    ]
