from django.urls import path
from .views import (
    create_category,
    get_category,
    get_categoryid,
    update_category,
    delete_category
)


urlpatterns = [
    path('create/', create_category, name='create_category'),
    path('get/', get_category, name='get_category'),
    path('getid/<int:pk>/', get_categoryid, name='get_categoryid'),
    path('update/<int:pk>/', update_category, name='update_category'),
    path('delete/<int:pk>/', delete_category, name='delete_category'),
]