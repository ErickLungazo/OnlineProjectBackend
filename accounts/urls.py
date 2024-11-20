from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import *

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("user/", UserInfoAPIView.as_view(), name="user-info")

]
