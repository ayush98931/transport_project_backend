from rest_framework.permissions import BasePermission

class isClient(BasePermission):
    message = "User must be a Client"
    def has_permission(self, request, view):
        
        print(request.POST)
        
        return True


class isTransporter(BasePermission):
    message = "User must be a Transporter"
    def has_permission(self, request, view):
        
        print(request.POST)
        
        return True
