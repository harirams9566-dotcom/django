from django.urls import path
from .views import (
    create_cart,
    get_cart,
    delete_cart,
    update_cart
)

urlpatterns = [
    path('create/', create_cart),
    path('get/', get_cart),
    path('delete/<int:pk>/', delete_cart),
    path('update/<int:pk>/', update_cart),
]