from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/otp_verification/', views.otp_verification, name='otp_verification'),
    path('profile/', views.profile_view, name='profile'),

]