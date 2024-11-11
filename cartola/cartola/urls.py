"""
URL configuration for cartola project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),  # página de admin 
    path('signup/', views.SignUpView.as_view(), name='signup'),  # criação de view
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("", views.home, name="home")
]

if settings.DEBUG:  # adiciona a opção de poder ver as imagens
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
