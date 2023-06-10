from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class RecentActivityView(LoginRequiredMixin,ListView):
    template_name = 'recent_activity/recent_activity.html'
    
    def get(self, request):
        return render(request, self.template_name)