from django.urls import path
from . import api_views

app_name = 'accounts'

urlpatterns = [
    path('account/login/', api_views.login_view, name='login'),
    path('account/create/parent/', api_views.register_parent_view, name='register_parent'),
    path('account/create/child/', api_views.register_child_view, name='register_child'),
    path('account/delete/', api_views.delete_account_view, name='delete_account'),
]
