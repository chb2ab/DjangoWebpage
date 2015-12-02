# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from vote.managers import VotableManager
import django

class Folder(models.Model):
	name = models.CharField(max_length=100)
	user = models.CharField(max_length=100, default="")
	def __str__(self):
		return self.name;

class Report(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	user = models.CharField(max_length=100)
	sd = models.CharField(max_length=200)
	ld = models.CharField(max_length=1000)
	public = models.BooleanField(default=False)
	folder = models.ForeignKey(Folder, null=True, default=None, blank=True)
	votes = VotableManager()
	def __str__(self):
		return self.name;
	
class Document(models.Model):
	report = models.ForeignKey(Report, null=True)
	name = models.CharField(max_length=100, null=True, default=None, blank=True)
	encrypted = models.BooleanField(default=False)
	docfile = models.FileField(upload_to='documents')
	def __str__(self):
		return str(self.name);
