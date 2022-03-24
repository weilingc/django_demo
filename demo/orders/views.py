from django.contrib import auth  # 用來找request.user的資料
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from allauth.account.decorators import verified_email_required
from cart.cart import Cart
from orders.models import Order, OrderItem
from shop import models

from . import forms


#讓顧客填寫收件資訊, 確認後創造一筆新訂單 
@login_required(login_url='/accounts/login/')
@verified_email_required
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        return render(request, 'product/index.html', locals())
    else:
        form = forms.OrderForm()
    return render(request, 'order/order_create.html', locals())

@login_required
@verified_email_required
def order_confirmed(request):
    form = forms.OrderForm(request.POST)
    cart = Cart(request)
    if request.method == 'POST':
        if form.is_valid:
            user = request.user
            full_name = request.POST['full_name']
            address = request.POST['address']
            postal_code = request.POST['postal_code']
            phone = request.POST['phone']
            total = cart.get_total_price()

            #先建立Order物件->再建立OrderItem物件
            neworder = Order(
                order_user = user,
                full_name = full_name,
                address = address,
                postal_code = postal_code,
                total = total,
                phone = phone,
            )
            neworder.save()
            for item in cart:
                orderitem = OrderItem(
                    order=neworder,
                    product=item['product'],
                    price=item['total_price'],
                    qty=item['quantity']
                )
                orderitem.save()
            cart.clear()
            return render(request, 'order/order_confirmed.html', locals())
    else:
        return redirect('/')


#顯示使用者現有訂單
def myorders(request):
    user = request.user
    orders = Order.objects.filter(order_user=user)
    return render(request, 'order/myorders.html', locals())

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order/order_detail.html', locals())
