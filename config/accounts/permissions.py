from rest_framework.permissions import BasePermission
from .models import ActiveToken


class IsTokenValid(BasePermission):

    def has_permission(self, request, view):

        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return False

        token = auth_header.split(" ")[1]

        return ActiveToken.objects.filter(token=token).exists()
