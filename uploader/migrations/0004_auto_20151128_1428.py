# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_group2_reports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group2',
            old_name='user',
            new_name='creator',
        ),
    ]
