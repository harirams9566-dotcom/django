from django.shortcuts import render

# Create your views here.
from .models import user
from .serializer import userserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST'])
def create_user(request):
    a=request.data.get('phone')
    s=request.data.get('email')
    d=request.data.get('password')
    c=request.data.get('confirm')
    serializer=userserializer(data=request.data)
    v=len(a)
    if v!=10:
        return Response({'error':'Invalid phone number'},status=status.HTTP_400_BAD_REQUEST)
    if user.objects.filter(email=s).exists():
        return Response({'error':'Email already exists'},status=status.HTTP_400_BAD_REQUEST)
    if d!=c:
        return Response({'error':'Passwords do not match'},status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login_user(request):
    s=request.data.get('email')
    d=request.data.get('password')
    
    if user.objects.filter(email=s).exists():
        c=user.objects.filter(email=s).first()
        if c.password == d:
            seri=userserializer(c)
            return Response({"message":"Login successful",'data':seri.data},status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid password"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error":"Email does not exist"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    s=user.objects.all()
    serializer=userserializer(s,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def get_userid(request,pk):
    s=user.objects.get(pk=pk)
    serializer=userserializer(s)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['PUT'])
def update_user(request,pk):
    s=user.objects.get(pk=pk)
    serializer=userserializer(s,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_user(request,pk):
    s=user.objects.get(pk=pk)
    s.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  
    
  