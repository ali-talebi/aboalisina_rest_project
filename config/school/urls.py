from django.urls import path 
from .views import View_Upload_Student_Information,View_Upload_Student_Education_Information


app_name = "school_app"
urlpatterns = [
    path('api/v1/upload_student_information/',View_Upload_Student_Information.as_view(),name="upload_student_information"),
    path("api/v1/upload_student_education_information/",View_Upload_Student_Education_Information.as_view(),name="upload_student_document_education"),
    
]
