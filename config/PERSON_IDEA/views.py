from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import School_Comments
from .serializers import School_Comments_Serializer

# Create your views here.

class Total_School_Views(APIView):
    """
    تمامی نظرات افراد در مورد مدرسه را برمیگرداند

    Args:
        پارامتری در اینجا نداریم
    """
    
    def get(self,request):
        total_schools_comments = School_Comments.objects.all()
        serializer = School_Comments_Serializer(instance=total_schools_comments,many=True)
        return Response(data=serializer.data)
    