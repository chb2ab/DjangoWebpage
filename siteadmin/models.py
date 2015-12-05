from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import django


# Create your models here.


class admin(models.Model):
	permissions = models.ManyToManyField(User)
