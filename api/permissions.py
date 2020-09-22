from rest_framework.permissions import BasePermission


class AdminResourcePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ('DELETE', 'POST', 'PATCH'):
            return request.user.is_staff
        return True
