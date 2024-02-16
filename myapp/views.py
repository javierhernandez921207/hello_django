from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Project, Task

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
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.values())
    return render(request, 'tasks.html', {'tasks': tasks})

def task(request, id):
    task = get_object_or_404(Task,id=id)    
    return HttpResponse(f'Task: {task.title} {task.description}')

def taskName(request, name):
    task = Task.objects.get(title=name)    
    return HttpResponse(f'Task: {task.title} {task.description}')