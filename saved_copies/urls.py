from django.urls import path
from . import views

urlpatterns = [
    path('', views.SavedCopiesView.as_view() , name='saved-copies'),
    
]