from django.urls import path
from . import views

urlpatterns = [
    path('ai-article-writer/keywords/', views.AiArticleWriterView.as_view() , name='ai article writer'),
    path('ai-article-writer/ideas/', views.IdeasGenratorView.as_view() , name='get ideas'),
    path('ai-article-writer/outlines/', views.OutlinesGenratorView.as_view() , name='get outlines'),
    path('ai-article-writer/article/', views.ArticleGenratorView.as_view() , name='get article'),
    
    
    path('email-tools/', views.EmailToolsView.as_view() , name='email tools'),
    path('SocialMedia-tools/', views.SocialMediaToolsView.as_view() , name='social media tools'),
    
]