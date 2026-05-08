from django.urls import path 
from .views import Total_Post_View,Total_Category_View


app_name = "blog"
urlpatterns = [
    path("api/v1/total_posts/",Total_Post_View.as_view(),name="total_posts"),
    path("api/v1/total_post_categoreis/",Total_Category_View.as_view(),name="total_post_category"),
    
    
]
