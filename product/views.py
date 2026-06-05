from .models import Product
from .serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Product created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product(request):
    category = request.query_params.get('category')
    sort = request.query_params.get('sort')
    find = request.query_params.get('find')

    s = Product.objects.all()

    if category:
        s = s.filter(category_id=category)

    if sort == 'low':
        s = s.order_by('price')

    elif sort == 'high':
        s = s.order_by('-price')

    if find:
        s = s.filter(product_name__icontains=find)

    serializer = ProductSerializer(
        s,
        many=True,
        context={'request': request}
    )

    return Response(
        {
            'message': 'data fetched successfully',
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_productid(request, pk):
    s = Product.objects.filter(pk=pk).first()

    if not s:
        return Response(
            {'message': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(s, context={'request': request})

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request, pk):
    s = Product.objects.filter(pk=pk).first()

    if not s:
        return Response(
            {'message': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(
        s,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, pk):
    s = Product.objects.filter(pk=pk).first()

    if not s:
        return Response(
            {'message': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    s.delete()

    return Response(
        {'message': 'Product deleted successfully'},
        status=status.HTTP_204_NO_CONTENT
    )