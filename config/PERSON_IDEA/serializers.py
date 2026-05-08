from rest_framework import serializers 
from .models import School_Comments

class School_Comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = School_Comments
        fields = "__all__"
