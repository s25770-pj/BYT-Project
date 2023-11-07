from django.urls import path
from . import api_views
from django.conf import settings

app_name = "accounts"

urlpatterns = [
]

if settings.DEBUG:
    urlpatterns += []
