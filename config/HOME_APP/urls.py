from django.urls import path 
from .views import Banner_Slider_View , LOGO_View 


urlpatterns = [
    path('api/v1/home/banner_sliders/',Banner_Slider_View.as_view(),name="home_banner_slider"),
    path('api/v1/logos/',LOGO_View.as_view(),name="logo_picture"),
    
        
]
