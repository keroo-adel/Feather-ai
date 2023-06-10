from django.urls import path
from . import views

urlpatterns = [
    path('ai-article-writer/keywords/', views.AiArticleWriterView.as_view() , name='ai article writer'),
    path('email-tools/', views.EmailToolsView.as_view() , name='email tools'),
    path('SocialMedia-tools/', views.SocialMediaToolsView.as_view() , name='social media tools'),
    
]