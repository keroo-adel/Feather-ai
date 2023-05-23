from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

User = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})

        try:
            User.objects.create_user(username, email, password)
        except ValueError:
            return render(request, 'accounts/register.html', {'error': 'Username or email already exists'})

        return HttpResponseRedirect(reverse('login'))

    else:
        return render(request, 'accounts/register.html')

def generate_otp():
    # Generate OTP logic
    otp = str(random.randint(100000, 999999))
    return otp

def send_otp(email, otp):
    # Send OTP logic
    # Implement your code to send the OTP via email, SMS, or any other method
    
    # This can be done using external libraries or services
    # For example, you can use Django's built-in email sending functionality or third-party libraries like SendGrid or Twilio
    # Replace this code with your actual OTP sending logic
    pass
    
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            # Perform login logic, e.g., set session or JWT token
            return redirect('home')  # Redirect to the home page after successful login
        return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})