
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSelfOrAdminOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admins can do anything
        if request.user.role == 'admin':
            return True

        # User can access only their own data
        if obj == request.user:
            return True

        # Staff can access other users (not admins)
        if request.user.role == 'staff' and obj.role != 'admin':
            return True

        return False



class IsAdminOrStaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in ['admin','staff']