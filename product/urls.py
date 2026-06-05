from django.urls import path
from .views import (
    create_product,
    get_product,
    get_productid,
    update_product,
    delete_product
)

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('get/', get_product, name='get_product'),
    path('getid/<int:pk>/', get_productid, name='get_productid'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
]