from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
