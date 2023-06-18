from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    name = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=False)
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Response(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='response')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
