from rest_framework import viewsets

from skills.models import Skill

from .serializers import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'slug'
