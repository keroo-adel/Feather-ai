from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import UserProfile
from django.utils import timezone
from datetime import timedelta
from .utils import send_otp_code, send_login_success_email
from django.contrib.auth.decorators import login_required

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
                authenticated_user.backend = 'django.contrib.auth.backends.ModelBackend'  # Set the backend attribute
                login(request, authenticated_user)
                messages.success(request, 'You have successfully logged in')
                send_login_success_email(authenticated_user)
                return redirect('home')
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

            otp_code = get_random_string(length=settings.OTP_CODE_LENGTH, allowed_chars='0123456789')
            user_profile, created = UserProfile.objects.get_or_create(user=User.objects.get(email=email))
            
            if not created:
                # User profile already exists, update the OTP code
                user_profile.otp_code = otp_code
                user_profile.otp_created_at = timezone.now()
                user_profile.save()

            send_otp_code(email, otp_code)

            # Store the email in the session
            request.session['otp_email'] = email

            # Render the OTP login form
            return redirect('otp_verification')

    else:
        return render(request, 'accounts/login.html')

def otp_verification(request):
    email = request.session.get('otp_email')  # Retrieve the email from the session

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

        # Check if the OTP code is expired (e.g., valid for 5 minutes)
        otp_expiry_time = user_profile.otp_updated_at + timedelta(minutes=5)
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

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
@login_required
def profile_view(request):
    # Retrieve the user profile or relevant information
    user = request.user
    # You can access the user's information, such as username, email, etc.
    username = user.username
    email = user.email

    # Render the profile template with the user's information
    return render(request, 'accounts/profile.html', {'username': username, 'email': email})