from rest_framework import serializers
from .models import Tasks, TaskUser


class TaskDetailSerializer(serializers.ModelSerializer):
    '''
       Создание сериалайзера post, put, delete для модели Task
    '''
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # Вставляет текущего пользователя

    class Meta:
        model = Tasks
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    '''
       Создание сериалайзера для просмотра всех записей для модели Task
    '''
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'user_id')


class TaskUserDetailSerializer(serializers.ModelSerializer):
    '''
       Создание сериалайзера post, put, delete для модели TaskUser
    '''

    class Meta:
        model = TaskUser
        fields = '__all__'


class TaskUserListSerializer(serializers.ModelSerializer):
    '''
       Создание сериалайзера для просмотра всех записей для модели TaskUser
    '''
    class Meta:
        model = TaskUser
        fields = ('id', 'task_id', 'id_user')