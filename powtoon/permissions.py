from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner.id == request.user.id or obj.shared_with.filter(pk=request.user.id):
            return True
        return False
