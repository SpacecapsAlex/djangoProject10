from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .forms import ProjectCreateForm

from .models import Project


# Create your views here.


def get_projects(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return render(
        request,
        'project/GetAllProjects.html',
        {'projects': projects}
    )


def create_project(request: HttpRequest) -> HttpResponse:
    # Получание заполненой формы
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = Project()
            project.title = form.cleaned_data['title']
            project.description = form.cleaned_data['description']
            project.email = form.cleaned_data['email']
            project.countUser = form.cleaned_data['countUser']
            project.save()

            return HttpResponseRedirect("/project/")
    # Получение формы для заполнения
    else:
        form = ProjectCreateForm()
    return render(
        request,
        'project/CreateProject.html',
        {'form': form}
    )
