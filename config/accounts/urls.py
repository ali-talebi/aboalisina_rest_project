from django.urls import path
from .views import CustomTokenObtainPairView, LogoutView,RegisterView,User_Information
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("information/",User_Information.as_view(),name="user_information"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
]
