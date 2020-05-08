from django.urls import path
from . import views


app_name = 'projects'
urlpatterns = [
    path('', views.ProjectListCreate.as_view()),
    path('skills/', views.skills_list, name="skills"),
    path('skill/<slug:slug>/', views.skills_detail, name="skill"),
    path('categories/', views.CategoryListCreate.as_view()),
    path('tech-stack/', views.TechStackListCreate.as_view()),
]
