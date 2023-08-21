from django.conf import settings
from django.db import models
class Location(models.Model):
    'Generated Model'
    name = models.CharField(max_length=255,)
    latitude = models.FloatField(null=True,blank=True,)
    longitude = models.FloatField(null=True,blank=True,)

# Create your models here.
