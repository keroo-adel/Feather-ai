
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.contrib.sites.shortcuts import get_current_site
import os

def send_otp_code(email, otp_code):
    subject = 'Feather.AI - Your OTP code'
    context = {'otp_code': otp_code,
                'otp_verification_url': f'http://localhost:8000/accounts/otp_verification/{otp_code}/',

               }
    body_html = render_to_string('accounts/otp_email.html', context)

    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = email

    msg = EmailMultiAlternatives(
        subject,
        '',
        from_email=from_email,
        to=[to_email]
    )

    msg.attach_alternative(body_html, "text/html")

    img_dir = os.path.join(settings.STATIC_ROOT, 'images')
    image = 'logo-feather-ai.png'
    file_path = os.path.join(img_dir, image)

    with open(file_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-ID', '<{name}>'.format(name=image))
        img.add_header('Content-Disposition', 'inline', filename=image)
        msg.attach(img)

    msg.send()
    

def send_login_success_email(user):
    subject = 'Login Successful'
    context = {'username': user.username}
    html_content = render_to_string('accounts/login_success_email.html', context)
    
    msg = EmailMultiAlternatives(subject, '', settings.DEFAULT_FROM_EMAIL, [user.email])
    msg.attach_alternative(html_content, "text/html")
    
    msg.send()

