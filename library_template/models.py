from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.TextField()

class Idea(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tone_of_voice = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    idea_text = models.TextField()


class Outline(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    Outlines = models.TextField()
    select_individual_outlines = models.BooleanField(default=False)

class Suboutline(models.Model):
    outline = models.ForeignKey(Outline, on_delete=models.CASCADE)
    suboutlines = models.TextField()
    subOutlineDescription = models.TextField()

class OutlineOrder(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    outline = models.ForeignKey(Outline, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
        
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    outlines = models.ManyToManyField('Outline', through='OutlineOrder')
    article_text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Additional fields for content and tags
    tags = models.CharField(max_length=100)
    
    def __str__(self):
        return self.article_text
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.outlines.all().delete()
        Topic.objects.filter(idea__outline__article=self).delete()
        Idea.objects.filter(outline__article=self).delete()
        super().delete(*args, **kwargs)