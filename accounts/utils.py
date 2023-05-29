
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.contrib.sites.shortcuts import get_current_site
import os
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def send_otp_code(request, email, otp_code):
    subject = 'Feather.AI - Your OTP code'
    context = {'otp_code': otp_code,
                'otp_verification_url': f'http://{get_current_site(request).domain}/accounts/otp_verification/{otp_code}/',
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
    

def send_login_success_email(request,user):
    subject = 'Login Successful'
    context = {'username': user.username,
               'url_homepage': f'http://{get_current_site(request).domain}/library/all/',
               }    
    body_html = render_to_string('accounts/login_success_email.html', context)

    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

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


def send_verification_email(request, user, token):
    current_site = get_current_site(request)
    subject = 'Verify Your Email'
    context = {'verification_link': f"http://{current_site.domain}/accounts/verify-email/{urlsafe_base64_encode(force_bytes(user.pk))}/{token}/",
               }    
    body_html = render_to_string('accounts/verify_email.html', context)

    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

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
    
    
   