from django.shortcuts import render
from projects.models import (
    Skill,
    Category,
    TechStack,
    Project
)
from .models import Service

# Create your views here.
def home(request):
    services = Service.objects.all()[:3]

    context = {
        'services': services
    }

    return render(request, 'main/home.html', context)

# def services(request):
#     context = {
#         'services': Service.objects.all()
#     }

#     return render(request, 'main/services.html', context)

# def service(request, slug):
#     context = {
#         'service': Service.objects.get(slug=slug)
#     }

#     return render(request, 'main/service.html', context)

def projects(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    context = {
        'title': 'projects',
        'skills': skills,
        'projects': projects
    }

    return render(request, 'main/projects.html', context)


def skill(request, slug):
    skill = Skill.objects.get(slug=slug)

    context = {
        'skill': skill
    }

    return render(request, 'main/skill.html', context)