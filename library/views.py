from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin , TemplateView):
    template_name = 'home/home.html'
    



