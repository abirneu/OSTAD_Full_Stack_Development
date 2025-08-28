from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    dob = models.DateField(null=True, blank=True)
    is_deleted= models.BooleanField(default=False) # Add this line

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='images/', blank=True)

    is_deleted= models.BooleanField(default=False) # Add this line

    def __str__(self):
        return self.name