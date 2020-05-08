"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    path('api/', include([
        path('services/', include('main.urls', namespace='services')),
        # path('projects/', include('projects.api.urls', namespace='projects')),
        path('skills/', include('skills.api.urls', namespace='skills')),
        path('clients/', include('clients.urls', namespace='clients')),
    ])),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
