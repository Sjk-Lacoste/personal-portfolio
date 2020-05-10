from rest_framework import routers

from skills.api.views import SkillViewSet
from clients.api.views import ClientViewSet
from main.api.views import ServiceViewSet
from projects.api.views import (
    CategoryViewSet,
    TechStackViewSet,
    ProjectViewSet
)

router = routers.DefaultRouter()

router.register('services', ServiceViewSet)
router.register('skills', SkillViewSet)
router.register('clients', ClientViewSet)
router.register('categories', CategoryViewSet)
router.register('tech-stack', TechStackViewSet)
router.register('projects', ProjectViewSet)
