from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('ai-article-writer', TemplateView.as_view(template_name='ai_article_writer/aIArticleWriter.html') , name='ai article writer'),
]