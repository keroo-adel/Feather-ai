from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecentActivityView.as_view() , name='recent-activity'),
]