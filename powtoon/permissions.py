from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner.id == request.user.id:
            return True
        if request.method in permissions.SAFE_METHODS:
            if obj.shared_with.filter(pk=request.user.id):
                return True
            groups = request.user.groups.all()
            if [group for group in groups if group.permissions.filter(code='perm-view-powtoon-not-shared-or-owner')]:
                return True
        else:
            groups = request.user.groups.all()
            if [group for group in groups if group.permissions.filter(code='perm-share-powtoon')]:
                return True
        return False
