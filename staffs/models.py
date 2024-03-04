from django.db import models
from django.utils import timezone

# Create your models here.
class Staff(models.Model):
    
    class Status(models.TextChoices):
        acastaff='AS', 'Academicstaff'
        nonstaff='NS', 'Non-Academicstaff'
        unkwon='Nil', 'NIL'
        
    staffname = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    nationality = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)
    dob = models.CharField(max_length=225)
    faculty = models.CharField(max_length=225)
    qualifification = models.CharField(max_length=225)
    department = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    salary = models.CharField(max_length=225)
    join_date = models.DateField(null=True)
    photo = models.CharField(max_length=225, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.unkwon)
    
    
    class Meta:
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields = ['-updated_at']),
        ]
    def __str__(self):
        return self.staffname