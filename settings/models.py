from django.contrib.auth.models import User
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    system_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='system_users')
    generation_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='generation_users')

    def __str__(self):
        return self.user.username