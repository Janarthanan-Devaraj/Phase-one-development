from user.models import User

from django.db import models

class Thread(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participant = models.ManyToManyField(
        User, related_name='participants', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.topic
    

class Responses(models.Model):
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body[0:50]
    

