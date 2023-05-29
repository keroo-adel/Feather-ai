from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('api/register/', views.UserRegistrationView.as_view(), name='api_register_user'),

]