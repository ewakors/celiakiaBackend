from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer
from main.models import Product, Category
from django.db.models import Q
from django.contrib.auth.models import User


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        key = self.request.GET.get('key', None)
        category = self.request.GET.get('category', None)

        products = Product.objects.filter(is_active=True)

        if category:
            products = products.filter(category=category)
        if key:
            products = products.filter(name__icontains=key) | products.filter(bar_code__icontains=key)
        return products

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
