from django.urls import path
from . import views
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]

if settings.DEBUG:
    urlpatterns += []
