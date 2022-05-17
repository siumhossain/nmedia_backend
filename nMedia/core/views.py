from cgitb import reset
from crypt import methods
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import  *
from .serializers import * 
from rest_framework import status 
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
@swagger_auto_schema(tags=['welcome'],methods=['get'],)

@api_view(['GET'])
def home(request):
    return JsonResponse({'msg':'hi'})



# get all news 
@swagger_auto_schema(tags=['Get all news'],methods=['get'])
@api_view(['GET'])
def getAllNews(request):
    try:
        obj = News.objects.all()
        serializer = NewsSerializer(obj,many=True)

        if not serializer.data:
            return Response("there is no data at this moment",status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_200_OK)
    except obj.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#get single news
@swagger_auto_schema(tags=['Get a single news'],methods=['get'])
@api_view(['GET'])
def getSingleNews(request,title):
    try:
        obj = News.objects.get(title=title)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NewsSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)


# post single news
@swagger_auto_schema(tags=['post news'],methods=['post'],request_body=NewsSerializer)
@api_view(['POST'])
def postNews(request):
    serializer = NewsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # print(data['title'])
    
    return JsonResponse({'msg':'ok'})

#create sub category
@swagger_auto_schema(tags=['create a sub category'],methods=['post'],request_body=SubCategorySerializer)
@api_view(['POST'])
def createSubCategory(request):
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(tags=['create a category'],methods=['post'],request_body=CategorySerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(tags=['get all category'],methods=['get'])
@api_view(['GET'])
@permission_classes([AllowAny])
def getAllCategory(request):
    try:
        obj = Category.objects.all()
        serializer = CategorySerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except obj.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(tags=['get all Subcategory'],methods=['get'])
@api_view(['GET'])
@permission_classes([AllowAny])
def getAllSubCategory(request):
    
        obj = SubCategory.objects.all()
        serializer = SubCategorySerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@swagger_auto_schema(tags=['Get a single subcategory'],methods=['get'])
@api_view(['GET'])
def getSingleSubCategory(request,id):
    try:
        obj = SubCategory.objects.filter(category__id = id)
    except SubCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SubCategorySerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@swagger_auto_schema(tags=['Get a single subcategory by title'],methods=['get'])
@api_view(['GET'])
def getSingleSubCategoryByTitle(request,title):
    try:
        obj = SubCategory.objects.get(title = title)
    except SubCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SubCategorySerializer(obj)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def createBanner(request):
    serializer = BannerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) 
@permission_classes([AllowAny])
def getBanner(request):
    
        obj = Banner.objects.all()
        serializer = BannerSerializer(obj,many=True)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   


    
@swagger_auto_schema(tags=['get content by id'],methods=['get'])

@api_view(['GET'])

def getSingleContent(request,id):
    
    try:
        obj = News.objects.get(id = id)
        
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NewsSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)



@swagger_auto_schema(tags=['top stories'],methods=['get'])
@api_view(['GET'])
def topStories(request,number):
    try:
        obj = News.objects.all()[:number]
        serializer = NewsSerializer(obj,many=True)

        if not serializer.data:
            return Response("there is no data at this moment",status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_200_OK)
    except obj.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

