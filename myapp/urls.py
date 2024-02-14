from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('hello/<str:user>', views.hello),
    path('projects', views.projects),
    path('tasks', views.tasks),
    path('task/<int:id>', views.task),
    path('task/<str:name>', views.taskName)
]


