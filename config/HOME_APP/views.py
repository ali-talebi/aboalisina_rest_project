from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import Banner_Slider
from .serializers import Banner_Slider_Serializer 

# Create your views here.



class Banner_Slider_View(APIView):
    
    def get(self,request):
        banners = Banner_Slider.objects.all()
        serializer = Banner_Slider_Serializer(instance=banners,many=True)
        return Response(data=serializer.data)
    
