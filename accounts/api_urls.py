from django.urls import path

from accounts.api_views import KidUserCreateView, ParentUserCreateView, ParentUserLoginView, KidUserLoginView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('kid/create/', KidUserCreateView.as_view(), name='kiduser_create'),
    path('kid/login/', KidUserLoginView.as_view(), name='kiduser_login'),
    path('parent/create/', ParentUserCreateView.as_view(), name='parentuser_create'),
    path('parent/login/', ParentUserLoginView.as_view(), name='parentuser_login'),
    path('user-details/', UserDetailView.as_view(), name='user-details'),
]
