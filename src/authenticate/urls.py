from django.urls import path
from .views import create_user, login_user, users_list

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('login-user/', login_user, name='login_user'),
    path('users-list/', users_list, name='users_list')
]
