from django.urls import path

from .views import get_projects

urlpatterns = [
    path('', get_projects),
]