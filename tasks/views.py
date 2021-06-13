from rest_framework import generics
from .models import TaskUser, Tasks
from .serializers import *
from .permissions import IsOwnerOrReadOnly


class TaskCreate(generics.CreateAPIView):
    '''
       Для создания записей модели Task
    '''
    serializer_class = TaskDetailSerializer


class TasksListView(generics.ListAPIView):
    '''
       Для просмотра всех записей модели Task
    '''
    serializer_class = TaskListSerializer
    queryset = Tasks.objects.all()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
       Обновление, просмотр и удаление записей одного обьекта модели Task
    '''
    serializer_class = TaskDetailSerializer
    queryset = Tasks.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)  # розграничиваем права доступа


class TaskUserCreate(generics.CreateAPIView):
    '''
       Для создания записей модели TaskUser
    '''
    serializer_class = TaskUserDetailSerializer


class TasksUserListView(generics.ListAPIView):
    '''
       Для просмотра всех записей модели TaskUser
    '''
    serializer_class = TaskUserListSerializer
    queryset = TaskUser.objects.all()


class TaskUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
       Обновление, просмотр и удаление записей одного обьекта модели TaskUser
    '''
    serializer_class = TaskUserDetailSerializer
    queryset = TaskUser.objects.all()

