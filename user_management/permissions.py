from rest_framework import permissions


class SiteAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.rank is 'ADM'
