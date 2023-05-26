from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    otp_code = models.CharField(max_length=6, blank=True)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    otp_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email