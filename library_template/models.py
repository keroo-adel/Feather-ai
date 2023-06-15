from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Topic(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.TextField()
    
    def __str__(self):
        return self.name

class Idea(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tone_of_voice = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    idea_text = models.TextField()
    
    def __str__(self):
        return self.idea_text


class Outline(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    Outlines = models.TextField()
    select_individual_outlines = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Outlines

class Suboutline(models.Model):
    outline = models.ForeignKey(Outline, on_delete=models.CASCADE)
    suboutlines = models.TextField( null=True, blank=True)
    body  = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.suboutlines

    
        
class Article(models.Model):
    title = models.CharField(max_length=200, blank=True)
    outlines = models.ManyToManyField('Outline')
    article_text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='articles_images/', blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # Additional fields for content and tags
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.outlines.all().delete()
        Topic.objects.filter(idea__outline__article=self).delete()
        Idea.objects.filter(outline__article=self).delete()
        super().delete(*args, **kwargs)
        
class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Saved Article: {self.article.title}"