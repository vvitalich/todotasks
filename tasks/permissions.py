from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
        Розграничивает доступ к заданиям. Что создал - то можно изменять и удалять
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user
