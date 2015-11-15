# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0005_auto_20151103_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='report',
            field=models.ForeignKey(null='', to='uploader.Report'),
        ),
    ]
