from rest_framework import permissions

class IsReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #ei review jodi user na kore thake
        #read korte parbe, update, delete
        #GET
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.reviewer == request.user
