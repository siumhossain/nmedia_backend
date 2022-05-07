from dataclasses import field, fields
from core.models import News
from rest_framework import serializers

from .models import *

class NewsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y : %I:%M %p",read_only=True)
    class Meta:
        model = News
        fields = ["id","subCategory","title","details","thumbnail","created","createdBy"]

class CreateNewsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y : %I:%M %p",read_only=True)
    class Meta:
        model = News
        fields = ["subCategory","title","details","thumbnail","createdBy"]


class SubCategorySerializer(serializers.ModelSerializer):
    newsCount = serializers.SerializerMethodField()
    news = serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = ["id","title","description","created","newsCount","news"]

    def get_newsCount(self, obj):
        count = News.objects.filter(subCategory__id = obj.id).count()
        return count
    def get_news(self,obj):
        news = News.objects.filter(subCategory__id = obj.id)
        serializer = NewsSerializer(news,many=True)
        return serializer.data
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(format="%d-%m-%Y : %I:%M %p",read_only=True)
    # image = serializers.SerializerMethodField()
    class Meta:
        model = Banner
        fields = ['id','title','description','image','createdAt',]
    # def get_image(self, banner):
    #         request = self.context.get('request')
    #         image = banner.image.url
    #         return request.build_absolute_uri(image)



            