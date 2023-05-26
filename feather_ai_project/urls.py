from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('pages.urls')),
    path('accounts/',include('accounts.urls')),
    path('library/', include('library.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),    
    path('social-auth/', include('social_django.urls', namespace='social')),

]
