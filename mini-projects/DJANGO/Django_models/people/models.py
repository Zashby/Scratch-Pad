from django.db import models

class State(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.
class Person(models.Model):
    #char field for string, must have max length
    first_name = models.CharField(max_length=20,)
    # null=True allows empty value in database
    # blank=True allows python to save empty values
    last_name = models.CharField(max_length=20, null=True, blank=True,)
    # models.PositiveIntegerField
    age = models.IntegerField(null=True, blank=True)
    is_close_friend = models.BooleanField( default=False)
    state=models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.first_name.title()