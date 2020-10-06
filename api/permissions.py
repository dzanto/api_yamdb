from rest_framework import permissions
from rest_framework.permissions import BasePermission


class AdminResourcePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('DELETE', 'PATCH'):
            return request.user.is_staff or request.user.rank == 'ADM'
        return True


class StaffResourcePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('DELETE', 'PATCH'):
            return request.user.is_staff or request.user.rank == 'MOD'
        return True


class IsOwnerOrReadOnly(BasePermission): 
    """ 
    Custom permission to only allow owners of an object to edit it. 
    """ 
 
    def has_object_permission(self, request, view, obj): 
        # Read permissions are allowed to any request, 
        # so we'll always allow GET, HEAD or OPTIONS requests. 
        if request.method in permissions.SAFE_METHODS: 
            return True 
 
        # Write permissions are only allowed to the owner of the snippet. 
        return obj.author == request.user 
