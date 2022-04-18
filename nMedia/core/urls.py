from urllib.parse import urlparse
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.home,name="home view test"),
    path('auth/',include('djoser.urls')),


    #get news
    path('getNews/',views.getAllNews,name   ="for get all the news"),

    #get single news 
    path('getNews/<str:title>/',views.getSingleNews,name="get single news"),

    #post news 
    path('postNews/',views.postNews,name="post news in database"),

    #create subcategory
    path('createSubCategory/',views.createSubCategory,name="create sub category"),
    #create category
    path('createCategory/',views.createCategory,name="create category"),

    #get all category
    path('getAllCategory/',views.getAllCategory,name="get all category"),

    #get all sub category
    path('getAllSubCategory/',views.getAllSubCategory,name="get all subcategory"),


    # create banner 
    path('createBanner/',views.createBanner,name="create banner for front page"),

    # get all banner
    path('getBanner/',views.getBanner,name="get all banner data"),

    # JWT authentication 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     # JWT authentication 
]