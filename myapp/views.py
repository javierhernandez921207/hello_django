from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Project, Task
from .forms import CreateNewProject, CreateNewTask
# Create your views here.
def index(request):
    title = 'My App'
    return render(request, 'index.html', {'title': title})

def about(request):
    return render(request, 'about.html')

def hello(request, user):
    return HttpResponse("Hello %s" % user)

def projects(request):
    projects  = list(Project.objects.values())
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.values())
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            task = Task(title=form.cleaned_data['title'], description=form.cleaned_data['description'], project_id=1)
            task.save()
            return redirect('tasks')
        else:
            return render(request, 'tasks/task_create.html', {'form': CreateNewTask()})
    return render(request, 'tasks/task_create.html', {'form': CreateNewTask()})

def create_project(request):
    if request.method == 'POST':
        form = CreateNewProject(request.POST)
        if form.is_valid():
            project = Project(name=form.cleaned_data['title'])
            project.save()
            return redirect('projects')
        else:
            return render(request, 'projects/project_create.html', {'form': CreateNewProject()})
    return render(request, 'projects/project_create.html', {'form': CreateNewProject()})

def update_task(request, id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            return redirect('tasks')
        else:
            return render(request, 'tasks/task_update.html', {'form': CreateNewTask(), 'task': task})
    return render(request, 'tasks/task_update.html', {'form': CreateNewTask(), 'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect('tasks')

def task(request, id):
    task = get_object_or_404(Task,id=id)    
    return HttpResponse(f'Task: {task.title} {task.description}')

def taskName(request, name):
    task = Task.objects.get(title=name)    
    return HttpResponse(f'Task: {task.title} {task.description}')