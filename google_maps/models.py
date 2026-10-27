# Create your models here.
from django.db import models

class Googlemaps(models.Model):
    title = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)


    def __str__(self):
        return self.title