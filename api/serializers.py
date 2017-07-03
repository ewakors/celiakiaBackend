
from rest_framework import serializers

from main.models import Product, Category
from django.contrib.sites.shortcuts import get_current_site


class ProductSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    gluten_free = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, instance):
        # site = get_current_site(None)
        # returning image url if there is an image else blank string
        return self.context['request'].build_absolute_uri(instance.image.url)

class ProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_image(self, instance):
        # site = get_current_site(None)
        return self.context['request'].build_absolute_uri(instance.image.url)


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
