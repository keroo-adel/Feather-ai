from rest_framework.views import APIView
from django.shortcuts import render

class LandingPageView(APIView):
    
    def get(self, request):
        return render(request, 'landing/landing.html')
    
class FeaturesPageView(APIView):
    
    def get(self, request):
        return render(request, 'landing/features.html')
    
    
class AboutPageView(APIView):
    
    def get(self, request):
        return render(request, 'landing/about.html')
    
class ContactPageView(APIView):
    
    def get(self, request):
        return render(request, 'landing/contact.html')
    
    