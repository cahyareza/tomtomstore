import random
from django.shortcuts import render, get_object_or_404
from .models import Product
from myproject.apps.cart.forms import CartAddProductForm


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_featured=True)
    related_products = list(Product.objects.all().filter(is_featured=True).exclude(id=product.id))
    if len(related_products) >= 5:
        related_products = random.sample(related_products, 4)

    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'related_products': related_products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'store/product_detail.html', context)