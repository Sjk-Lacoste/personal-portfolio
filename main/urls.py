from django.urls import path
from django.conf import settings
from django.conf.urls import static
from . import views

app_name = 'services'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.ServiceListCreate.as_view()),
    # path('<slug>/', service, name='service'),
]
