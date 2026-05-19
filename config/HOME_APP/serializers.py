from rest_framework import serializers 
from .models import Banner_Slider , LOGO 


class Banner_Slider_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Banner_Slider
        fields = "__all__"
        


class LOGO_SERIALIZER(serializers.ModelSerializer):
    
    class Meta:
        model  = LOGO
        fields = ['name','logo_picture']

    
