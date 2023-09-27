from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from test_front.views import MainView

schema_view = get_schema_view(
    openapi.Info(
        title='BYT Project',
        default_version=settings.REST_API_VER,
        description='API for BYT Project'
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/'+settings.REST_API_VERSION, include([
        path('accounts/', include('accounts.api_urls', namespace='api_accounts'))
    ])),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', MainView.as_view(), name='main-default-global')
]
