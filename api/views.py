from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer
from main.models import Product, Category


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('name')
    serializer_class = ProductSerializer

    def get_queryset(self):
        key = self.request.GET.get('key', None)
        category = self.request.GET.get('category', None)

        products = Product.objects.filter(is_active=True)

        if category:
            products = products.filter(category=category).order_by('name')
        if key:
            products = products.filter(name__icontains=key).order_by('name') | products.filter(bar_code__icontains=key).order_by('name')
        return products


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
