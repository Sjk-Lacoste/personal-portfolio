from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.skills_list, name="skills"),
    path('skill/<slug:slug>/', views.skills_detail, name="skill"),
    path('categories/', views.CategoryListCreate.as_view()),
    path('tech-stack/', views.TechStackListCreate.as_view()),
    path('projects/', views.ProjectListCreate.as_view()),
]
