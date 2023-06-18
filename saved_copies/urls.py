from django.urls import path
from . import views

urlpatterns = [
    path('', views.SavedCopiesView.as_view() , name='saved-copies'),
    path('delete/<int:pk>', views.DeleteArticleView.as_view(), name='delete_article'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/step3/<int:pk>/', views.ArticleDetailPrev1View.as_view(), name='article-step3'),
    path('article/step2/<int:pk>/', views.ArticleDetailPrev2View.as_view(), name='article-step2'),
    path('article/step1/<int:pk>/', views.ArticleDetailPrev3View.as_view(), name='article-step1'),
    path('export-pdf/<int:article_id>/', views.ExportPDFView.as_view(), name='export_pdf'),

]