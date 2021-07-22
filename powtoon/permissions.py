from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    This permission checks if the logged in user can perform some action.
    Only the owner of powtoon, a user with shared access or a user with necessary permissions can access a powtooon.
    Only the owner of powtoon or a user with necessary permissions can edit or share a powtooon.
    """
    def has_object_permission(self, request, view, obj):
        """The powtoon owner will always have access"""
        if obj.owner.id == request.user.id:
            return True
        """Checking if the request is GET, OPTIONS or HEAD, if so it will not need to change powtoon data."""
        if request.method in permissions.SAFE_METHODS:
            """As this user does not own the powtoon, checking if this user has access to this powtoon."""
            if obj.shared_with.filter(pk=request.user.id):
                return True
            """As this user does not own powtoon and is not included in the share, we check if he has sufficient 
            permissions for this."""
            groups = request.user.groups.all()
            if [group for group in groups if group.permissions.filter(code='perm-view-powtoon-not-shared-or-owner')]:
                return True
        else:
            """Checking if the user has sufficient permissions to share or edit this powtoon."""
            groups = request.user.groups.all()
            if [group for group in groups if group.permissions.filter(code='perm-share-powtoon')]:
                return True
        return False
