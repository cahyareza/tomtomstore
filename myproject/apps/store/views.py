from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_featured=True)
    related_products = list(Product.objects.all().filter(is_featured=True).exclude(id=product.id))
    if len(related_products) >= 6:
        related_posts = random.sample(related_products, 5)

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)