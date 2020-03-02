from django.shortcuts import render
from .models import (
    Skill,
    Category,
    TechStack,
    Project
)

# Create your views here.
def projects(request):
    projects = Project.object.all()
    skills = Skill.objects.all()

    context = {
        'skills': skills,
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)


def skill(request, slug):
    skill = Skill.objects.get(slug=slug)

    context = {
        'skill': skill
    }

    return render(request, 'projects/skill.html', context)