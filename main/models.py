from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=255)
    image = models.FileField(upload_to='category_images',null=True, blank=True)
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Name', max_length=255)
    bar_code = models.CharField('Bar code', max_length=255,unique=True)
    gluten_free = models.BooleanField(default=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete= models.CASCADE)
    is_active = models.BooleanField('isActive', default=False)
    image = models.FileField(upload_to='product_images', null=True, blank=True)
    REQUIRED_FIELDS = ['name', 'barcode']

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField('Name', max_length=255)
    image = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

# class User (models.Model):
#     email = models.EmailField('Email',max_length=255,unique=True)
#     username = models.CharField('Login', max_length=255, unique=True)
#     password = models.CharField('Password', max_length=255)
#     REQUIRED_FIELDS = ['username', 'password']