from .models import Category
from .serializer import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'Category created successfully', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(
        categories,
        many=True,
        context={'request': request}
    )

    return Response(
        {
            'message': 'Categories fetched successfully',
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_categoryid(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {'message': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = CategorySerializer(category, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()

        return Response(
            {'message': 'Category deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

    except Category.DoesNotExist:
        return Response(
            {'message': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['PUT'])
def update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {'message': 'Category not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = CategorySerializer(
        category,
        data=request.data,
        partial=True,
        context={'request': request}
    )
    
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message': 'Category updated successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)