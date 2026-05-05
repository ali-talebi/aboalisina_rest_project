from rest_framework import serializers 
from .models import Banner_Slider 


class Banner_Slider_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Banner_Slider
        fields = "__all__"
        

