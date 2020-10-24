from django.urls import path
from . import views
from .views import TaskList as TaskListView


urlpatterns = [    
    path('home/', TaskListView.as_view(),name='TODO-POSTS' ),
]