from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=200)

class Block(models.Model):
    character = models.CharField(max_length=1)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    count = models.IntegerField()
