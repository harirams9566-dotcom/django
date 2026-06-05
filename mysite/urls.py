from django.urls import path
from .views import (
    create_user,
    login_user,
    get_users,
    get_userid,
    update_user,
    delete_user
)

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('login/', login_user, name='login_user'),
    path('get/', get_users, name='get_users'),
    path('getid/<int:pk>/', get_userid, name='get_userid'),
    path('update/<int:pk>/', update_user, name='update_user'),
    path('delete/<int:pk>/', delete_user, name='delete_user'),
]