from django.db import models

# Create your models here.
from django.db import models

class Block(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    html = models.TextField( blank=True, null=True)
    tag = models.CharField(max_length=10, default='p')

class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    # Add other fields as needed for your Article model

    def __str__(self):
        return self.title

class Block2(models.Model):
    BLOCK_TYPES = (
        ('h1Style', 'Heading 1'),
        ('h2Style', 'Heading 2'),
        ('h3Style', 'Heading 3'),
        ('paragraphStyle', 'Paragraph'),
        ('listStyle', 'Bullet List'),
    )

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='blocks', null=True)
    content = models.CharField(max_length=255)
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES)
    position = models.TextField()

    def __str__(self):
        return self.content