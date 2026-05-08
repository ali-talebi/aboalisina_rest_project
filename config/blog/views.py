from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .models import Post,Post_Category
from .serializers import Post_Category_Serializer,Post_Serializer

# Create your views here.


class Total_Category_View(APIView):
    """تمامی دسته بندی  و پستهای مربوط به آن دسته بندی را بر میگرداند

    Args:
        APIView (_type_): _description_
    """
    
    def get(self,request):
        total_post_category = Post_Category.objects.all()
        serializer = Post_Category_Serializer(instance =total_post_category,many=True)
        return Response(data=serializer.data)
    


class Total_Post_View(APIView):
    """ تمامی پستهای وبسایت را برمیگرداند

    Args:
        APIView (_type_): _description_
    """
    def get(self,request):
        total_posts = Post.objects.all()
        serializer = Post_Serializer(instance=total_posts,many=True)
        return Response(data=serializer.data)
    
        