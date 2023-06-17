from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.

class ChangeLanguage(LoginRequiredMixin, ListView):
    template_name = 'user_settings/changeLanguage.html'
    def get(self, request):
        return render(request,self.template_name)
    
class ProfileDetailsView(LoginRequiredMixin, ListView):
    template_name = 'user_settings/ProfileDetails.html'
    def get(self, request):
        return render(request,self.template_name)