from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # login process
    path('login/', views.login_view, name='login'),
    path('login/otp_verification/', views.otp_verification, name='otp_verification'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),
    path('otp_verification/<str:otp_code>/', views.otp_verification_url, name='otp_verification_url'),
    path('verify-email/<str:uidb64>/<str:token>/', views.EmailVerificationView.as_view(), name='verify_email'),

    # Register process
    path('register/', views.RegisterView.as_view(), name='register'),
    path('check_email/', TemplateView.as_view(template_name='accounts/check_email.html'), name='check_email'),
    
    
    # Profile
    path('profile/', views.profile_view, name='profile'),

]