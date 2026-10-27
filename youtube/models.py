# Create your models here.
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title