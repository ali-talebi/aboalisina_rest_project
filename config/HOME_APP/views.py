from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import Banner_Slider , LOGO
from .serializers import Banner_Slider_Serializer , LOGO_SERIALIZER 
from drf_yasg.utils import swagger_auto_schema

# Create your views here.



class Banner_Slider_View(APIView):
    @swagger_auto_schema(tags=["Slider Picture/Video"])
    def get(self,request):
        
        """ تصاویر اولیه وبسایت را برمیگرداند

        Returns:
            _type_: _description_
        """
        
        banners = Banner_Slider.objects.all()
        serializer = Banner_Slider_Serializer(instance=banners,many=True)
        return Response(data=serializer.data)
    

class LOGO_View(APIView):
    
    def get(self,request):
        total_logos = LOGO.objects.all()
        serializer = LOGO_SERIALIZER(instance=total_logos,many=True)
        return Response(data=serializer.data)