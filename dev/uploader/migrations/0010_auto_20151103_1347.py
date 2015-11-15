# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0009_report_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='report',
            field=models.ForeignKey(to='uploader.Report', blank=True),
        ),
    ]
