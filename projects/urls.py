from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.SkillListCreate.as_view()),
    path('categories/', views.CategoryListCreate.as_view()),
    path('tech-stack/', views.TechStackListCreate.as_view()),
    path('projects/', views.ProjectListCreate.as_view()),
]
