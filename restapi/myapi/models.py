from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    edad = models.IntegerField(default=0)
    altura = models.IntegerField(default=0)
    peso = models.IntegerField(default=0)
    def __str__(self):
        return self.name