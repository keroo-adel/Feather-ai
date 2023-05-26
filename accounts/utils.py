
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail


def send_otp_code(email, otp_code):
    subject = 'Feather.AI - Your OTP code'
    context = {'otp_code': otp_code}
    html_content = render_to_string('accounts/otp_email.html', context)

    msg = EmailMultiAlternatives(subject, '', to=[email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    

def send_login_success_email(user):
    subject = 'Login Successful'
    context = {'username': user.username}
    html_content = render_to_string('accounts/login_success_email.html', context)
    
    msg = EmailMultiAlternatives(subject, '', settings.DEFAULT_FROM_EMAIL, [user.email])
    msg.attach_alternative(html_content, "text/html")
    
    msg.send()

