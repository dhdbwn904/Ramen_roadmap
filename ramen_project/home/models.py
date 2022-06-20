from operator import mod
from statistics import mode
from django.db import models
from django.forms import URLField
from django.utils import timezone
import datetime

# Create your models here.

class Restaurent(models.Model):
    name = models.CharField(max_length=50, unique=True)
    point = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)
    img = models.CharField(max_length=300, default='')
    review = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name

