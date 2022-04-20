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
    class Meta:
        model = SubCategory
        fields = "__all__"

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



            