# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_document_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='report',
            field=models.ForeignKey(to='uploader.Report'),
        ),
    ]
