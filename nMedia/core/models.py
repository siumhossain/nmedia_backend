from email.policy import default
from unicodedata import category
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class NewUser(AbstractUser):
    username  = models.CharField(max_length=250,unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']





class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]


class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created"]


class News(models.Model):
    subCategory = models.ForeignKey('SubCategory',on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=300,unique=True)
    details = models.TextField()
    thumbnail = models.ImageField(upload_to="newsThumbnail/",null=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)
    embeddedLink = models.TextField(null=True,blank=True)
        #  there goes user 
    createdBy = models.TextField(null=True,blank=True)
        #  there goes user     
    class Meta:
        ordering = ["-created"]



class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="bannerImage")
    createdAt = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        ordering = ["-createdAt"]



