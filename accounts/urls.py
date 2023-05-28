from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/otp_verification/', views.otp_verification, name='otp_verification'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),
    path('otp_verification/<str:otp_code>/', views.otp_verification_url, name='otp_verification_url'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile_view, name='profile'),

]