
from rest_framework import serializers

from django.contrib.auth.models import User

from main.models import Product, Category



class ProductSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    gluten_free = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

#
#
# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(style={'input_type': 'password'})
#
#     def _validate_username(self, username, password):
#         user = None
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#         else:
#             msg = _('Must include "username" and "password".')
#             raise exceptions.ValidationError(msg)
#
#         return user
#
#     class Meta:
#         model = User
#         fields = ("username", "password")
