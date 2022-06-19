from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Restaurent(models.Model):
    name = models.CharField(max_length=50, unique=True)
    point = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

