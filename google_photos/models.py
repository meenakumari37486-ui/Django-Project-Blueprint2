from django.db import models

# Create your models here.

class Googlephotos(models.Model):
    title = models.CharField(max_length=100)
    edit = models.IntegerField(default=0)


    def __str__(self):
        return self.title