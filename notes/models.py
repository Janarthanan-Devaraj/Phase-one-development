from django.db import models

from user.models import User


class Department(models.Model):    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Semester(models.Model):

    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    ]
    
    name = models.CharField(max_length=200, blank=True, choices = SEMESTER_CHOICES)
    
    def __str__(self):
        return self.name

class Notes(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null= True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null= True)
    subject = models.CharField(max_length=200,blank=True, null=True)
    unit = models.CharField(max_length=200,blank=True, null=True)
    pdf = models.FileField(upload_to='notes', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)