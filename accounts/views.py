from django.contrib.auth.views import LoginView, FormView 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import UserProfile
from django.utils import timezone
from datetime import timedelta
from .utils import send_otp_code, send_login_success_email, send_verification_email
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.views.generic import CreateView ,View
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str

############## login methods #############
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        with_password = False
        if 'with_password=true' in request.get_full_path():
            with_password = True
        

        if with_password:
            # Authenticate with email and password
            users = User.objects.filter(email=email)
            authenticated_user = None
            for user in users:
                if user.check_password(password):
                    authenticated_user = user
                    break

            if authenticated_user is not None:
                if authenticated_user.is_active:
                    
                    authenticated_user.backend = 'django.contrib.auth.backends.ModelBackend'  # Set the backend attribute
                    login(request, authenticated_user)
                    messages.success(request, 'You have successfully logged in')
                    return redirect('home')
                
                else :
                    messages.error(request, 'virify your email')
                    return redirect('login')
            
            else:
                messages.error(request, 'Invalid email or password')
                return redirect('login')

        else:
            # Generate a new OTP code and send it to the user's email address
            if not email:
                query_params = {'with_password': 'true'}
                query_string = urlencode(query_params)
                redirect_url = f"{reverse('login')}?{query_string}"
                return redirect(redirect_url)

            try:
                user = User.objects.get(email=email)
                user_profile, created = UserProfile.objects.get_or_create(user=user)

                if created or not user_profile.otp_code:
                    otp_code = get_random_string(length=settings.OTP_CODE_LENGTH, allowed_chars='0123456789')
                    user_profile.otp_code = otp_code

                user_profile.otp_created_at = timezone.now()
                user_profile.save()

                send_otp_code(request, email, user_profile.otp_code)

                # Store the email in the session
                request.session['otp_email'] = email

                # Render the OTP login form
                return redirect('otp_verification')

            except User.DoesNotExist:
                messages.error(request, 'You do not have an account. Please register to be able to login.')
                return redirect('register')


            except User.DoesNotExist:
                messages.error(request, 'You do not have an account. Please register to be able to login.')
                return redirect('register')

    else:
        return render(request, 'accounts/login.html')

def otp_verification(request):
    email = request.session.get('otp_email') 

    if not email:
        messages.error(request, 'Email not found')
        return redirect('login')

    if request.method == 'POST':
        otp_code = request.POST.get('otp_code')

        if not otp_code:
            messages.error(request, 'Please provide OTP code')
            return redirect('otp_verification')

        # Check if the OTP code and email match
        user_profile = UserProfile.objects.filter(user=User.objects.get(email=email), otp_code=otp_code).first()

        if user_profile is None:
            messages.error(request, 'Invalid OTP code')
            return redirect('otp_verification')

        # Check if the OTP code is expired (e.g., valid for 60 minutes)
        otp_expiry_time = user_profile.otp_updated_at + timedelta(hours=1)
        if otp_expiry_time < timezone.now():
            messages.error(request, 'OTP code has expired')
            return redirect('otp_verification')

        # Clear the session variable
        del request.session['otp_email']

        # Authenticate and login the user
        user = user_profile.user
        if user is not None:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')

        messages.error(request, 'Invalid OTP code')
        return redirect('otp_verification')

    return render(request, 'accounts/otp_verification.html')

def otp_verification_url(request, otp_code):
    email = request.session.get('otp_email')  # Retrieve the email from the session

    if not email:
        messages.error(request, 'Email not found')
        return redirect('login')

    # Check if the OTP code is provided
    if not otp_code:
        messages.error(request, 'Please provide OTP code')
        return redirect('otp_verification')

    # Check if the OTP code and email match
    user_profile = UserProfile.objects.filter(user=User.objects.get(email=email), otp_code=otp_code).first()

    if user_profile is None:
        messages.error(request, 'Invalid OTP code')
        return redirect('otp_verification')

    # Check if the OTP code is expired (e.g., valid for 60 minutes)
    otp_expiry_time = user_profile.otp_updated_at + timedelta(hours=1)
    if otp_expiry_time < timezone.now():
        messages.error(request, 'OTP code has expired')
        return redirect('otp_verification')

    # Clear the session variable
    del request.session['otp_email']

    # Authenticate and login the user
    user = user_profile.user
    if user is not None:
        if not user.is_active:
            user.is_active = True
        
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('home')

    messages.error(request, 'Invalid OTP code')
    return redirect('otp_verification')

############## register methods #############
class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        # Retrieve form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
    
        with_password = False
        if 'with_password=true' in request.get_full_path():
            with_password = True


        # Check if email already exists in User model
        if User.objects.filter(email=email).exists():
            messages.error(request, 'You already have an account. Please log in.')
            return redirect('login')

        if with_password:
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
                
            # Check if password and confirm password match
            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')

            # Validate password strength
            try:
                validate_password(password)
            except Exception as e:
                messages.error(request, str(e))
                return redirect('register')

            # Create the new user (inactive)
            user = User.objects.create_user(username=full_name, email=email, password=password)
            user.first_name, user.last_name = full_name.split(' ', 1)
            user.is_active = False  # Mark user as inactive
            user.save()

            # Generate verification token
            token = default_token_generator.make_token(user)

        
            send_verification_email(request, user, token)
            messages.success(request, 'Please check your email to verify your account.')

            # Redirect to email verification page
            return redirect('check_email')
        else:
            
            otp_code = get_random_string(length=6, allowed_chars='0123456789')
            
            # Create the new user (inactive)
            user = User.objects.create_user(username=full_name, email=email)
            user.first_name, user.last_name = full_name.split(' ', 1)
            user.save()
            
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            if created or not user_profile.otp_code:
                otp_code = get_random_string(length=settings.OTP_CODE_LENGTH, allowed_chars='0123456789')
                user_profile.otp_code = otp_code

            user_profile.otp_created_at = timezone.now()
            user_profile.save()

            send_otp_code(request, email, user_profile.otp_code)

            # Store the email in the session
            request.session['otp_email'] = email

            # Render the OTP login form
            return redirect('otp_verification')
    
class EmailVerificationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            # Log in the user
            authenticated_user = authenticate(request, username=user.email, password=user.password)
            if authenticated_user is not None:
                login(request, authenticated_user) 
                return redirect('home')
            messages.success(request, 'Email verification successful. You are now logged in.')
        else:
            messages.error(request, 'Invalid email verification link.')

        return redirect('home')  
    
############## profile methods #############

@login_required
def profile_view(request):
    # Retrieve the user profile or relevant information
    user = request.user
    # You can access the user's information, such as username, email, etc.
    username = user.username
    email = user.email

    # Render the profile template with the user's information
    return render(request, 'accounts/profile.html', {'username': username, 'email': email})