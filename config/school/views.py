from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .serializers import StudentInformation_Serializer,StudentEducationInformation_Serializer
from .models import StudentInformation,StudentEducationInformation
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .permissions import IsClient 

# Create your views here.


class View_Upload_Student_Information(APIView):
    
    permission_classes = [IsAuthenticated,IsClient]
    
    """ مربوط به مدارک هویتی دانش آموز

    Args:
        APIView (_type_): _description_
    """
    @swagger_auto_schema(tags=["Student Information"])
    def get(self, request):
        """دریافت اطلاعات هویتی دانش آموز

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        student = StudentInformation.objects.filter(client=request.user).first()
    
        if student:
            serializer = StudentInformation_Serializer(instance=student)
            return Response(data=serializer.data)
    
        return Response({"message": "No information yet"})
    @swagger_auto_schema(tags=["Student Information"])
    def post(self,request):
        """بارگذاری اطلاعات هویتی دانش آموز

        Args:
            APIView (_type_): _description_
        """
        serializer = StudentInformation_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    @swagger_auto_schema(tags=["Student Information"])
    def patch(self, request):
        """تغییرات جزئی اطلاعات و مدارک هویتی

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        information_student = StudentInformation.objects.filter(client=request.user).first()
        
        if not information_student:
            return Response({'errors':'Information not Found'},status=404)
        
        serializer = StudentInformation_Serializer(instance=information_student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    @swagger_auto_schema(tags=["Student Information"])
    def put(self, request):
        information_student = StudentInformation.objects.filter(client=request.user).first()
        
        if not information_student:
            return Response({'errors':'Information not Found'},status=404)
        
        serializer = StudentInformation_Serializer(instance=information_student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    

class View_Upload_Student_Education_Information(APIView):
    
    
    permission_classes = [IsAuthenticated,IsClient]
    
    """مربوط به مدارک تحصیلی دانش آموز

    Args:
        APIView (_type_): _description_
    """
    @swagger_auto_schema(tags=["Student Education"])
    def get(self,request):
        student = StudentEducationInformation.objects.filter(client=request.user).first()
        if student:
            serializer = StudentEducationInformation_Serializer(instance=student)
            return Response(data=serializer.data)
        return Response({"message": "No information yet"})
    @swagger_auto_schema(tags=["Student Education"])
    def post(self,request):
        serializer = StudentEducationInformation_Serializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    
    @swagger_auto_schema(tags=["Student Education"])
    def patch(self,request):
        student = StudentEducationInformation.objects.filter(client=request.user).first()
        
        if student:
            serializer = StudentEducationInformation_Serializer(instance=student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            return Response(serializer.errors)
        
        return Response({"message": "No information yet"})

    @swagger_auto_schema(tags=["Student Education"])
    def put(self,request):
        student = StudentEducationInformation.objects.filter(client=request.user).first()
        
        if student:
            serializer = StudentEducationInformation_Serializer(instance=student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            return Response(serializer.errors)
        
        return Response({"message": "No information yet"})
    
    @swagger_auto_schema(tags=["Student Education"])
    def delete(self,request):
        student = StudentEducationInformation.objects.filter(client=request.user).first()
        
        if student:
            student.delete()
            return Response({"message":"delete successfully"})
        return Response({"message": "No information yet"})
        
                
        
        
        
        