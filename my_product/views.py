from django.http import Http404
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from .models import Product


def productpagedef(request):


    content = {

    }
    return render(request,"products/product_list.html", content)

class productpageclass(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.get_active_products()


def product_detail(request, *args , **kwargs):
    product_id = kwargs ['productId']
    product_name = kwargs ['name']

    product = Product.objects.get_by_id(product_id)
    if product is None or not product.active :
        raise Http404("محصول مورد نظر یافت نشد")
    else:
        context = {
            'product': product,
            

        }
        return render(request, "products/product_detail.html", context)



class searchproductlist(ListView):


    template_name = 'products/product_list.html'
    # paginate_by = 2

    def get_queryset(self):
        request = self.request
        qs = request.GET.get("q")
        if qs is not None:
            return Product.objects.filter(title__icontains=qs)
        else:
            return Product.objects.filter(active=False)


def info(request):

    context = {}

    return render(request, "products/info.html", context)
