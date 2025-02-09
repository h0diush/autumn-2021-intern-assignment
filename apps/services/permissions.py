from rest_framework.permissions import SAFE_METHODS, BasePermission


class AdminCreatOrUserRead(BasePermission):
    def has_permission(self, request, view):
        if request.method == SAFE_METHODS[0]:
            return True
        if (request.user.is_superuser == True
                and request.user.is_staff == True):
            return True
        return False
