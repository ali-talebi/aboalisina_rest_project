from rest_framework import serializers 
from .models import Post,Post_Category

class Post_Category_Serializer(serializers.ModelSerializer):
    
    
    total_posts = serializers.SerializerMethodField(read_only=True)
    
    def get_total_posts(self,post_object):
        return Post_Serializer(post_object.posts.all(),many=True).data
    
    class Meta:
        model = Post_Category
        fields = "__all__"
        

class Post_Serializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField(read_only=True) 
    
    class Meta:
        model = Post 
        fields = "__all__"
        
