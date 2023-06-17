from django.urls import path
from . import views

urlpatterns = [
    path('change_language', views.ChangeLanguage.as_view() , name='change_language'),
    path('profile', views.ProfileDetailsView.as_view() , name='Profile_Details'),
]