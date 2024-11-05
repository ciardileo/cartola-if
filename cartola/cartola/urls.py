"""
URL configuration for cartola project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # página de admin 
]

if settings.DEBUG:  # adiciona a opção de poder ver as imagens
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
