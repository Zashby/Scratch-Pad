from django.db import models

# Create your models here.

class manyTypes(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=150)
    image_back = models.CharField(max_length=150)
    types = models.CharField(max_length=50)
    many_types = models.ManyToManyField(manyTypes, related_name='pokemon', blank=True) 
    def __str__(self):
        return self.name