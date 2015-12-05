# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_group2_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='group2',
            name='reports',
            field=models.ManyToManyField(to='uploader.Report'),
        ),
    ]
