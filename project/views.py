from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .forms import ProjectCreateForm, ProjectFilterForm

from .models import Project


# Create your views here.


def get_projects(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    filter_form = ProjectFilterForm()
    return render(
        request,
        'project/GetAllProjects.html',
        {'projects': projects, 'filter': filter_form}
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


def delete_project(request: HttpRequest, project_id: int) -> HttpResponse:
    project = Project.objects.get(id=project_id)
    project.delete()
    # переход по ссылке на страницу(/project/) - глобальный url
    return HttpResponseRedirect("/project/")


def filter_projects(request: HttpRequest) -> HttpResponse:
    form = ProjectFilterForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        countUser = form.cleaned_data['countUser']
        projects = (Project.objects
                    .filter(title=title)
                    .filter(countUser=countUser))
        return render(
            request,
            'project/GetAllProjects.html',
            {'projects': projects, 'filter': form}
        )
