from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import path
from .api_views import login_view

app_name = 'api_accounts'

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]