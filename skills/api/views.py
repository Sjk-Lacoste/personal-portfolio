from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from skills.models import Skill

from .serializers import SkillSerializer

@api_view(['POST', ])
def api_create_skill_view(request):
    skill = Skill
    if request.method == "POST":
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
def api_detail_skill_view(request, slug):
    try:
        skill = Skill.objects.get(slug=slug)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_skill_view(request, slug):
    try:
        skill = Skill.objects.get(slug=slug)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SkillSerializer(skill, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Skill have been successfully updated"
            return Response(data=data)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_skill_view(request, slug):
    try:
        skill = Skill.objects.get(slug=slug)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = skill.delete()
        data = {}
        if operation:
            data["success"] = "Skill have been deleted successfully"
        else:
            data["failure"] = "Something wrong happened when you tried to deleted this skill"

        return Response(data=data)
