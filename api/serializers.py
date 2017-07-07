
from rest_framework import serializers
from django.conf import settings
from main.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    image = serializers.SerializerMethodField()
    gluten_free_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, instance):
        if instance.image:
            image = instance.image.url
        else:
            image = settings.STATIC_URL + 'images/znakZap.jpg'
        return self.context['request'].build_absolute_uri(image)

    def get_gluten_free_image(self, instance):
        if instance.gluten_free:
            image = settings.STATIC_URL + 'images/glutenFree.png'
        else:
            image = settings.STATIC_URL + 'images/gluten.jpg'
        return self.context['request'].build_absolute_uri(image)


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
        return self.context['request'].build_absolute_uri(instance.image.url)
