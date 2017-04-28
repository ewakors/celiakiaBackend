from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from .serializers import ProductSerializer, CategorySerializer
from main.models import Product, Category
from django.db.models import Q
from django.contrib.auth.models import User


# class UserList(generics.ListCreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    # permission_classes = (IsAdminUser,)
#
#    def get_queryset(self):
#        username = self.request.GET.get('username', None)
#        if username:
#            return User.objects.filter(username=username)
#        return User.objects.all()
#

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        key = self.request.GET.get('key', None)
        # bar_code = self.request.GET.get('barcode', None)
        # name = self.request.GET.get('name', None)

        return Product.objects.filter(Q(bar_code=key) | Q(name=key))

# class ProductCreateView(generics.ListCreateAPIView):
#     model = Product
#
#     fields = ['name', 'barcode', 'gluten_free', 'category']
#
#     def get_success_url(self):
#         return reverse_lazy("api:product", kwargs={'pk': self.object.id})