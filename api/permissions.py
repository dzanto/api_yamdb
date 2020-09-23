from rest_framework.permissions import BasePermission


class AdminResourcePermission(BasePermission):

    def has_permission(self, request, view):
        print(request.method)
        if request.method in ('DELETE', 'POST', 'PATCH'):
            return request.user.is_staff
        return True
