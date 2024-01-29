from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .api_views import LoginView, LogoutView, RegisterView, UserDataListView

app_name = 'api_accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/get/', UserDataListView.as_view(), name='get_user_data'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
