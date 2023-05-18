from rest_framework.views import APIView
from django.shortcuts import render

class LandingPageView(APIView):
    
    def get(self, request):
        return render(request, 'landing/landing.html')