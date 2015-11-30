# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Group2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('sd', models.CharField(max_length=200)),
                ('ld', models.CharField(max_length=1000)),
                ('public', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(to='uploader.Folder', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='report',
            field=models.ForeignKey(to='uploader.Report', null=True),
        ),
    ]
