from django.urls import path

from .views import get_projects, create_project, delete_project, filter_projects

urlpatterns = [
    path('', get_projects),
    path('create/', create_project),
    path('delete/<int:project_id>/', delete_project),
    path('filter/', filter_projects),
]
