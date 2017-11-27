from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Block(models.Model):
    character = models.CharField(max_length=2)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    count = models.IntegerField()

# Should return the information of most limited chracters are:
# No, missing x character
# looping through all the fonts and return message for each one
# A calculation function to display how much character left for the input
# A message to see how much it is needed to print out the input if failed
# Go check with the input message and how many characters left in the database, return differet meassage based on different input

## Some wild cards
# Related to how many characters are more often used in today's world
# Heat Maps
