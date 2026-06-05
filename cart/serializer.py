from rest_framework import serializers
from .models import Cart
from product.serializer import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'