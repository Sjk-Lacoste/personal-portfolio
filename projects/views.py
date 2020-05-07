from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import (
    SkillSerializer,
    CategorySerializer,
    TechStackSerializer,
    ProjectSerializer
)

from .models import (
    Skill,
    Category,
    TechStack,
    Project
)


# Create your views here.
@api_view(['GET', 'POST'])
def skills_list(request):
    """
    List skills, or create a new skill
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        skills = Skill.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(skills, 10)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = SkillSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/skills/?page=' + str(nextPage), 'prevlink': '/api/skills/?page=' + str(previousPage)})
    elif request.method == 'POST':
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def skill_detail(request, slug):
    """
    Retrieve, update or delete a skill by slug.
    """
    try:
        skill = Skill.objects.get(slug=slug)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SkillSerializer(skill,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SkillSerializer(skill, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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