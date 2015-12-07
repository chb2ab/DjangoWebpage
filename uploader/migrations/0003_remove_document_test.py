# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_document_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='test',
        ),
    ]
