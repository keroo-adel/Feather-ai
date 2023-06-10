from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('pages.urls')),
    path('accounts/',include('accounts.urls')),
    path('library/', include('library.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),    
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('long_form_editor/', include('long_form_editor.urls')),
    path('chat_feather/', include('chat_feather.urls')),
    path('template/', include('library_template.urls')),
    path('saved-copies/', include('saved_copies.urls')),
    path('recent-activity/', include('recent_activity.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
