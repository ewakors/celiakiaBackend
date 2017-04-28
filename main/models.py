from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Name', max_length=255)
    bar_code = models.CharField('Bar code', max_length=255)
    gluten_free = models.BooleanField(default=False)

    user = models.ManyToManyField(User)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class User (models.Model):
    email = models.EmailField('Email',max_length=255,unique=True)
    username = models.CharField('Login', max_length=255, unique=True)
    password = models.CharField('Password', max_length=255)
    REQUIRED_FIELDS = ['username', 'password']