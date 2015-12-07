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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100, default=None, blank=True, null=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('docfile', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Group2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100, default='')),
                ('permissions', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100, default='')),
                ('sd', models.CharField(max_length=200)),
                ('ld', models.CharField(max_length=1000)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('public', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(null=True, to='uploader.Folder', default=None, blank=True)),
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
