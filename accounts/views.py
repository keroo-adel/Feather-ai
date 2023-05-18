from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class LoginView(LoginView):
    template_name = 'accounts/login.html'

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)