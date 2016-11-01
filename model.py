from django.db import models

class Letter(models.Model):
    first_name = models.CharField(max_length = 256)
