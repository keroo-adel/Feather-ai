from django.db import models

# Create your models here.
from django.db import models

class Block(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    html = models.TextField()
    tag = models.CharField(max_length=10, default='p')
