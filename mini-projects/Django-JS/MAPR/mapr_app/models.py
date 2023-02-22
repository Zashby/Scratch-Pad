from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Location(models.Model):
    latitude = models.DecimalField(decimal_places=5, max_digits=7)
    longitude = models.DecimalField(decimal_places=5, max_digits=8)
    timezone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
    



class Group(models.Model):
    name = models.CharField(max_length=30)
    private = models.BooleanField(default=True)
    pass

    def __str__(self):
        return self.name



class User(AbstractUser):
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(Group, related_name='users', blank=True)
    private = models.BooleanField(default=True)
    restricted = models.BooleanField(default=False)

    def __str__(self):
        return self.username




