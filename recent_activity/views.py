from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RecentActivity

class RecentActivityView(LoginRequiredMixin,ListView):
    model = RecentActivity
    template_name = 'recent_activity/recent_activity.html'
    context_object_name = 'activities'
    ordering = ['-timestamp']
    paginate_by = 10  # Set the number of activities to display per page
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply any additional filtering or custom logic to the queryset if needed
        return queryset