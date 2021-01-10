from importlib.resources import path

from my_product.views import  productpageclass, productpagedef, product_detail, searchproductlist, info

from django.urls import path, include




urlpatterns = [

    path('product-def',productpagedef ),
    path('info',info ),
    path('product-detail/<productId>/<name>', product_detail),
    path('product',productpageclass.as_view() ),
    path('product/search',searchproductlist.as_view() ),

]