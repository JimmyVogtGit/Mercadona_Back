from django.urls import path
from .views import create_user, LoginView, user_list

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('users-list/', user_list, name='users_list'),
    path('login-user/', LoginView.as_view(), name='login'),

]
