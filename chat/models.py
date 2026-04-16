from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} - {self.timestamp}'