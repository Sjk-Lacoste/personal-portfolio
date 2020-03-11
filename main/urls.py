from django.urls import path
from django.conf import settings
from django.conf.urls import static
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('api/services/', views.ServiceListCreate.as_view()),
    # path('services/', services, name='service'),
    # path('<slug:slug>/', service, name='service'),
    # path('portfolio/', views.projects, name='projects'),
    # path('skill/<slug:slug>/', views.skill, name='skill'),
]
