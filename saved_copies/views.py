from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class SavedCopiesView(LoginRequiredMixin,ListView):
    template_name = 'saved_copies/saved_copies.html'
    
    def get(self, request):
        return render(request, self.template_name)