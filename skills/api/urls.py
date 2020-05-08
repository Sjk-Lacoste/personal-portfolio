from django.urls import path

from .views import (
    api_detail_skill_view,
    api_update_skill_view,
    api_delete_skill_view,
    api_create_skill_view
)

app_name = 'skills'

urlpatterns = [
    path('create', api_create_skill_view, name='create'),
    path('<slug>/', api_detail_skill_view, name='view'),
    path('<slug>/update/', api_update_skill_view, name='update'),
    path('<slug>/delete', api_delete_skill_view, name='delete'),
]
