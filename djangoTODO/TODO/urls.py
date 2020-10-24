from django.urls import path
from . import views
from .views import TaskList as TaskListView
from .views import CreateTask as CreateTaskView


urlpatterns = [    
    path('', TaskListView.as_view(),name='TODO-POSTS' ),
    path('new/', CreateTaskView.as_view(),name='TODO-CREATE' ),
]