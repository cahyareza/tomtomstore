from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from ..store.models import Product, Payment

@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

    print(cart)

    return redirect('cart:cart_detail')

def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    payments = Payment.objects.all()
    cart = Cart(request)
    context = {
        'cart': cart,
        'payments': payments
    }
    return render(request, 'cart/cart.html', context)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'cart/success.html')


