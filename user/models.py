from django.db import models
from django.contrib.auth.models import AbstractUser
from indian_cities.dj_city import cities


class User(AbstractUser):

    GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ]

    username = models.CharField(max_length=200, unique=True)
    profile_pic = models.ImageField(upload_to="profile-pics", blank=True, null=True, default='profile-pics/default-img.png')
    profile_cover = models.ImageField(upload_to="profile-cover", blank=True, null=True, default='profile-cover/default-profile-cover.jpg')
    type = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male', null=True)
    dob = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class AcademicsInfo(models.Model):

    DEGREE_CHOICES = [
        ('B.Tech', 'Bachelor of Technology'),
        ('B.E', 'Bachelor of Engineering'),
        ('M.Tech', 'Master of Technology'),
        ('B.Sc', 'Bachelor of Science'),
        ('M.E', 'Master of Engineering'),
        ('M.Tech', 'Master of Technology'),
    ]

    DEPARTMENT_CHOICES = [
        ('IT', 'Information Technology'),
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    roll_number = models.CharField(max_length=7, blank=True, unique=True)
    degree = models.CharField(max_length=100, blank=True, choices=DEGREE_CHOICES)
    department = models.CharField(max_length=100, blank=True, choices=DEPARTMENT_CHOICES)
    current_semester = models.CharField(max_length=200, blank=True)
    cgpa = models.FloatField(max_length=3, blank=True)

class CompanyInfo(models.Model):

    STATE_CHOICES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    location = models.CharField(choices=cities, null=False, max_length=20)
    salary = models.BigIntegerField(blank=True)
