from rest_framework import routers

from skills.api.views import SkillViewSet
from clients.api.views import ClientViewSet

router = routers.DefaultRouter()

router.register('skills', SkillViewSet)
router.register('clients', ClientViewSet)
