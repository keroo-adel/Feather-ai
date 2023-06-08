from django.db import models

class CardTemplate(models.Model):
    template_id = models.IntegerField(unique=True)
    icon = models.FileField(upload_to='card_icons', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    bookmarked = models.BooleanField(default=False)
    tags = models.CharField(max_length=255, blank=True, null=True)  
    additional_photo = models.FileField(upload_to='photos/', blank=True, null=True)
    CATEGORY_CHOICES = [
        ('articles-and-blogs', 'articles-and-blogs'),
        ('ads-and-marketing-tools', 'ads-and-marketing-tools'),
        ('emial-letters', 'emial-letters'),
        ('writing-tools', 'writing-tools'),
        ('social-media', 'social-media'),
        ('sales-copy', 'sales-copy'),
        ('digital-ad-copy', 'digital-ad-copy'),
        ('brain-storming-tools', 'brain-storming-tools'),
        ('presonal-tools', 'presonal-tools'),
        ('startup-tools', 'startup-tools'),
        ('website-copy', 'website-copy'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES , blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)# Additional photo field
    def __str__(self):
        return self.title
