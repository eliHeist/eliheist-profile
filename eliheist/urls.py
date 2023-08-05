from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls', namespace='frontend')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('downloads/', include('downloads.urls', namespace='downloads')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)