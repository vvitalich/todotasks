from django.urls import path
from .views import *

app_name = "tasks"

urlpatterns = [
    path('task/create/', TaskCreate.as_view()),
    path('all/', TasksListView.as_view()),
    path('task/detail/<int:pk>/', TaskDetailView.as_view()),
    path('taskuser/create/', TaskUserCreate.as_view()),
    path('taskuser/all/', TasksUserListView.as_view()),
    path('taskuser/detail/<int:pk>/', TaskUserDetailView.as_view()),
]