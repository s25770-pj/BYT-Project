from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/'+settings.REST_API_VERSION, include([
        path('accounts/', include('accounts.api_urls', namespace='api_accounts'))
    ])),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
