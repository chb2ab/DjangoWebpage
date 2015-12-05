# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group2',
            name='permissions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
