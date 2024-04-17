from django.db import models
import datetime 
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='student_profiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(default='Adresss')
    fees_Permonth = models.FloatField(default=0.0)
    remaining_fees = models.FloatField(default=0.0)
    assignement = models.FileField(upload_to='student_assignments/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class EmailModel(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
