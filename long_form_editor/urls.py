from django.urls import path
from . import views

urlpatterns = [
    path('', views.LongFormEditorView.as_view(), name='long_form_editor'),
    path('api/save-article-title/', views.SaveArticleTitleView.as_view(), name='save_article_title'),
    path('api/create-block/', views.CreateBlockView.as_view(), name='create_block'),
    path('api/ask-feather/', views.AskFeatherView.as_view(), name='ask_feather'),

]