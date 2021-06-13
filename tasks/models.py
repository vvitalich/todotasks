from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Tasks(models.Model):
    '''
        Основная модель.
    '''
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name='Автор задачи')
    title = models.CharField(max_length=50, verbose_name='Задача')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    image = models.ImageField(blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.title


class TaskUser(models.Model):
    '''
        Вспомогательная модель. Задаче назначается исполнитель.
    '''
    id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE,
                                related_name='get_tasks', verbose_name='Задание')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Исполнитель')

    class Meta:
        ordering = ['task_id']

    def __str__(self):
        return self.task_id.title




