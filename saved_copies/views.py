from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from library_template.models import Article


class SavedCopiesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'saved_copies/saved_copies.html'
    context_object_name = 'saved_articles'
        
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).prefetch_related(
            'outlines__suboutline_set'
        )