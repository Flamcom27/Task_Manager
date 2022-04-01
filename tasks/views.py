from django.views.generic import ListView
from django.shortcuts import render
from .models import Task

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'