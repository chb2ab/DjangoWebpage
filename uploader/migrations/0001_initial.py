# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(default=None, max_length=100, blank=True, null=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('docfile', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group2',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(default='', max_length=100)),
                ('permissions', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(default='', max_length=100)),
                ('sd', models.CharField(max_length=200)),
                ('ld', models.CharField(max_length=1000)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('public', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(default=None, to='uploader.Folder', blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='group2',
            name='reports',
            field=models.ManyToManyField(to='uploader.Report'),
        ),
        migrations.AddField(
            model_name='document',
            name='report',
            field=models.ForeignKey(to='uploader.Report', null=True),
        ),
    ]
