# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0007_auto_20151103_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='longDescr',
            new_name='ld',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='shortDescr',
            new_name='sd',
        ),
    ]
