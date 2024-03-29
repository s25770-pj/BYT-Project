from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="REST APIs",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path('swagger(?P<format>)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/'+settings.REST_API_VERSION, include([
        path('accounts/', include('accounts.api_urls', namespace='api_accounts')),
        path('tests/', include('tests.api_urls', namespace='api_tests')),
    ])),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
