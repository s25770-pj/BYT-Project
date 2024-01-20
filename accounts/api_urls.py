from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth.views import MyObtainTokenPairView
from django.urls import path
from .api_views import CustomLoginView, LogoutView, RegisterView, UserDataView

app_name = 'api_accounts'

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user-data/', UserDataView.as_view(), name='user-data'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]