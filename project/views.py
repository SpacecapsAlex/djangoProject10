from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Project


# Create your views here.


def get_projects(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return render(
        request,
        'project/GetAllProjects.html',
        {'projects': projects}
    )
