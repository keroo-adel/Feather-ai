from django.shortcuts import render
from django.views.generic import ListView,View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CardTemplate
from django.shortcuts import redirect
from django.db.models import Q

class HomeView(LoginRequiredMixin , ListView):
    template_name = 'home/home.html'
    model = CardTemplate
    context_object_name = 'card_templates'
    def get_queryset(self):
        # Get the default queryset
        queryset = super().get_queryset()
        
        # Order the queryset to show bookmarked cards first
        queryset = queryset.order_by('-bookmarked', 'id')
        
        return queryset


        
        
class BookmarkToggleView(View):
    def get(self, request, card_template_id):
        card_template = CardTemplate.objects.get(id=card_template_id)
        card_template.bookmarked = not card_template.bookmarked
        card_template.save()
        return redirect('home')


# class SearchView(ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'card_templates'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             return CardTemplate.objects.filter(
#                             Q(title__icontains=query) | Q(description__icontains=query)
                
#             )
#         else:
#             return CardTemplate.objects.none()
        

class FilterByCategoryView(ListView):
    model = CardTemplate
    template_name = 'home/home.html'
    context_object_name = 'card_templates'

    def get_queryset(self):
        category = self.kwargs.get('category')
        subcategory = self.kwargs.get('subcategory')
        
        queryset = CardTemplate.objects.filter(Q(category=category) | Q(subcategory=category))
            
        
        return queryset