from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ..store.models import Product
from ..webpage.models import Testimoni

# Create your views here.

def frontpage(request):
    products = Product.objects.filter(is_featured=1)
    testimonis = Testimoni.objects.all()

    paginator = Paginator(products, 4)  # 3 posts in each page
    page = request.GET.get('page', 1)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        product_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        product_list = paginator.page(paginator.num_pages)

    context = {
        "product_list": product_list,
        "products": products,
        'testimonis': testimonis,
    }

    return render(request, 'frontpage.html', context)

