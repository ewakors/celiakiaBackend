from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
#display category in panel admin
    filter_horizontal = ("category",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)