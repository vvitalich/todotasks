from django.contrib import admin
from tasks.models import Tasks, TaskUser


class TasksAdmin(admin.ModelAdmin):
    '''
        Представление полей в админке
    '''
    list_display = ('id', 'title', 'user_id', 'created_at', 'updated_at')
    actions = None


class TaskUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_id', 'id_user')


admin.site.register(Tasks, TasksAdmin)
admin.site.register(TaskUser, TaskUserAdmin)
