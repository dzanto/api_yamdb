from rest_framework import permissions


class SiteAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.rank == 'ADM'


class SiteStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.rank == 'MOD' or request.user.rank == 'ADM'
