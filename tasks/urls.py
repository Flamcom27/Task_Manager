from tokenize import Name
from django.urls import path
from .views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name="home"),    
]
