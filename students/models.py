from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    class Status(models.TextChoices):
        fulltime = 'FT', 'FULLTIME'
        parttime = 'PT', 'PARTTIME'
        sandwich = 'SW', 'SANDWICH'
        unknown = 'UN', 'UNKNOWN'
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    gp = models.CharField(max_length=100)
    admitted = models.DateField(auto_now=True)
    upload = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.unknown)
    
    class Meta:
        ordering =['-upload']
        indexes = [
            models.Index(fields = ['upload']),
            ]
    def __str__(self):
        return self.name