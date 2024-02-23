from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about', views.about, name='about'),
    path('hello/<str:user>', views.hello, name='hello'),
    path('projects', views.projects, name='projects'),
    path('projects/<int:id>', views.detail_project, name='project_detail'),
    path('project_create', views.create_project, name='project_create'),
    path('tasks', views.tasks, name='tasks'),
    path('task/<int:id>', views.task, name='task'),
    path('task_create', views.create_task, name='task_create')
]


