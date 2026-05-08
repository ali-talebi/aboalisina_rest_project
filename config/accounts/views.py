from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer
from .models import ActiveToken
from django.contrib.auth.models import User 




class RegisterView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "username": serializer.validated_data['username'],
                "status": "success",
                "message": "User created successfully. Now you can login."
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return Response({"error": "No token"}, status=400)
        token = auth_header.split(" ")[1]
        ActiveToken.objects.filter(user=request.user, token=token).delete()

        return Response({"message": "Logged out successfully"}, status=200)



class User_Information(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return Response({"user":f"{request.user.username}"})
        