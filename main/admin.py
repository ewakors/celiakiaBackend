from django.contrib import admin
from .models import Product, Category, Image


class ProductAdmin(admin.ModelAdmin):
#display category in panel admin
    # filter_horizontal = ("category",)
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Image)