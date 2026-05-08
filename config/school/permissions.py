from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    
    def has_permission(self,request,view,obj):
        
        user = request.user 
        
        if not user.is_authenticated:
            return False 
        return request.user == obj.client 
    