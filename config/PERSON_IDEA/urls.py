from django.urls import path 
from .views import Total_School_Views


app_name = "person_idea_app"
urlpatterns = [
    path('api/v1/total_schools_comments/',Total_School_Views.as_view(),name="total_school_view"),
    
]
