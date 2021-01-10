from django.contrib import admin

# Register your models here.
from my_product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active', "image", ]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
