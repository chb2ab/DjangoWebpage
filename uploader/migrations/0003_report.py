# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20151103_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('shortDescr', models.CharField(max_length=200)),
                ('longDescr', models.CharField(max_length=1000)),
                ('public', models.BooleanField(default=False)),
            ],
        ),
    ]
