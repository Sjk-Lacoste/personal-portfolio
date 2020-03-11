from django.shortcuts import render
from .models import (
    Skill,
    Category,
    TechStack,
    Project
)

from .serializers import (
    SkillSerializer,
    CategorySerializer,
    TechStackSerializer,
    ProjectSerializer
)
from rest_framework import generics


# Create your views here.
class SkillListCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TechStackListCreate(generics.ListCreateAPIView):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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