from rest_framework import viewsets

from projects.models import (
    Category,
    TechStack,
    Project
)

from .serializers import (
    CategorySerializer,
    TechStackSerializer,
    ProjectSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class TechStackViewSet(viewsets.ModelViewSet):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer
    lookup_field = 'slug'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
