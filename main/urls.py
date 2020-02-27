from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='service'),
    path('<slug:slug>/', service, name='service')
]
