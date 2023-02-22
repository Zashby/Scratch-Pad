from django.db import models

from assignments.models import Assignment

letter_grades = [
    ('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D'),('F', 'F'),
]


# Create your models here.
class Students(models.Model):
    assignments = models.ManyToManyField(Assignment, blank=True,related_name='students')
    name = models.CharField(max_length=50)
    letter_grade = models.CharField(max_length=1,choices=letter_grades, default = "")
    number_grade = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name