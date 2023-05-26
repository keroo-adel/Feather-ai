from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/otp_verification/', views.otp_verification, name='otp_verification'),
    path('profile/', views.profile_view, name='profile'),

]