from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer, ImageSerializer
from main.models import Product, Category, Image
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
        return Product.objects.filter(is_active=True).filter(Q(bar_code=key) | Q(name=key) | Q(category=category))


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
