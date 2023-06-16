from django.urls import path
from . import views

urlpatterns = [
    path('ai-article-writer/keywords/', views.AiArticleWriterView.as_view() , name='ai article writer'),
    path('ai-article-writer/keywords/save_topic_keywords/', views.SaveTopicKeywordsView.as_view(), name='save_topic_keywords'),

    
    path('ai-article-writer/ideas/', views.IdeasGenratorView.as_view() , name='get ideas'),
    path('ai-article-writer/ideas/save_ideas/', views.SaveIdeasView.as_view() , name='save_ideas'),

    path('ai-article-writer/outlines/', views.OutlinesGenratorView.as_view() , name='get outlines'),
    path('ai-article-writer/outlines/save_outlines/', views.SaveOutlinesView.as_view() , name='save_outlines'),

    
    path('ai-article-writer/article/', views.ArticleGenratorView.as_view() , name='get article'),
    
    
    path('email-tools/', views.EmailToolsView.as_view() , name='email tools'),
    path('email-tools/delete/<int:email_subject_id>/', views.DeleteEmailSubjectView.as_view(), name='delete_email_subject'),

    path('SocialMedia-tools/', views.SocialMediaToolsView.as_view() , name='social media tools'),
    
]