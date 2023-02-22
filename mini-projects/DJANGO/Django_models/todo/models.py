from django.db import models

#Import for User model
from django.contrib.auth.models import User

class Priority(models.Model):
    name = models.CharField(max_length=10, )
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.priority} - {self.name}"

# Create your models here.
class TodoItem(models.Model):
    text = models.CharField(max_length=240)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todos')
    date_completed = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    #User model inclusion
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.text[0:20]
