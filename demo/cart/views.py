from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from shop import models

from .cart import Cart
from .forms import CartAddProductForm

# from shop.models import Category, Product



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return redirect('cart-url')     #返回頁面

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    cart.remove(product)
    return redirect('cart-url')     #返回頁面

# @login_required
def cart_detail(request):
    cart = Cart(request)
    # 使用 for in 的時候，他會開始迭代，並且呼叫 `__iter__`
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity':item['quantity'],
                'update':True
            })
    return render(request,'cart/cart_detail.html', locals())
