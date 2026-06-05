from .models import Cart
from .serializer import CartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_cart(request):
    user = request.data.get('user')
    product = request.data.get('product')
    quantity = request.data.get('quantity')

    carts = Cart.objects.filter(
        users_id=user,
        products_id=product
    )

    if carts.exists():
        return Response(
            {'message': 'Cart already exists'},
            status=status.HTTP_200_OK
        )

    Cart.objects.create(
        users_id=user,
        products_id=product,
        quantity=quantity
    )

    return Response(
        {'message': 'Cart added successfully'},
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def get_cart(request):
    user_id = request.query_params.get('cart')

    carts = Cart.objects.all()

    if user_id:
        carts = carts.filter(users_id=user_id)

    serializer = CartSerializer(
        carts,
        many=True,
        context={'request': request}
    )

    return Response(
        {
            'message': 'Data fetched successfully',
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
def delete_cart(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(
            {'message': 'Cart not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    cart.delete()

    return Response(
        {'message': 'Cart deleted successfully'},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['PUT'])
def update_cart(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(
            {'message': 'Cart not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    action = request.data.get('action')

    if action == 'increase':
        cart.quantity += 1

    elif action == 'decrease':
        if cart.quantity > 1:
            cart.quantity -= 1

    else:
        return Response(
            {'message': 'Invalid action'},
            status=status.HTTP_400_BAD_REQUEST
        )

    cart.save()

    serializer = CartSerializer(cart)

    return Response(
        {
            'message': 'Cart updated successfully',
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )