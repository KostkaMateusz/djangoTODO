from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Task
# Create your views here.



class TaskList(ListView):
    model=Task
    
 

class CreateTask(CreateView):
   model=Task
   fields=['title','contex'] 