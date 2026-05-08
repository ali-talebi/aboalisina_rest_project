from rest_framework import serializers
from .models import StudentInformation,StudentEducationInformation


class StudentInformation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInformation 
        fields = "__all__"
        
        
class StudentEducationInformation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEducationInformation
        fields = "__all__"
        