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
        return Product.objects.filter(is_active=True).filter(Q(bar_code=key) | Q(name=key) | Q(category=category))



class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


    # def add_new_product(self,name,bar_code,gluten_free,category):
    #     product = Product()
    #     product.name = name
    #     product.bar_code = bar_code
    #     product.gluten_free = gluten_free
    #     product.category = category
    #     return product