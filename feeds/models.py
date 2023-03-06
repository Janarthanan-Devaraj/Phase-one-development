from django.db import models

from user.models import User
from django.urls import reverse
from django.utils.timezone import now

class Feed(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
