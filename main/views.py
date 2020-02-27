from django.shortcuts import render
from .models import Service

# Create your views here.
def home(request):
    context = {
        'services': Service.objects.all()[:3]
    }

    return render(request, 'main/home.html', context)

def services(request):
    context = {
        'services': Service.objects.all()
    }

    return render(request, 'main/services.html', context)

def service(request, slug):
    context = {
        'service': Service.objects.get(slug=slug)
    }

    return render(request, 'main/service.html', context)