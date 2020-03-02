from django.urls import path
from django.conf import settings
from django.conf.urls import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('services/', services, name='service'),
    # path('<slug:slug>/', service, name='service'),
    path('portfolio/', projects, name='projects'),
    path('skill/<slug:slug>/', skill, name='skill'),
]
