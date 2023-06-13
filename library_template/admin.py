from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_text', 'user', 'created_at')
    
    search_fields = ('article_text',)