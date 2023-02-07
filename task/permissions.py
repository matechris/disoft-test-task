from rest_framework.permissions import BasePermission, SAFE_METHODS

from task.models import Task


class IsAuthenticatedOrIsAdmin(BasePermission):
    """
    If user is admin, they have all permissions;
    if user is the author of some tasks, they can modify these tasks;
    other users can only view tasks.
    """

    def has_permission(self, request, view):
        user_id = request.user.id
        tasks = Task.objects.prefetch_related().filter(author=user_id)

        return bool(
            (request.method in SAFE_METHODS and
             request.user and
             request.user.is_authenticated)
            or (request.user and request.user.is_staff)
            or (request.user and len(tasks) >= 1)
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_staff
