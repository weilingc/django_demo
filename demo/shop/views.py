from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm

from . import models


#首頁
def index(request):
    products = models.Product.objects.all()
    return render(request, 'shop/index.html', locals())

#選定目錄後並轉跳至其頁面
def sort_by_category(request, category_id):     #header.html中的 {% url 'category-url' cate.id %} --> 對應到urls --> urls再向此視圖函數發出request
    products = models.Product.objects.filter(category=category_id).order_by('id')
    cate_name = models.Category.objects.get(id=category_id)

    paginator = Paginator(products,12)
    p = request.GET.get('p')
    try:
        p_products = paginator.page(p)
    except PageNotAnInteger:
        p_products = paginator.page(1)
    except EmptyPage:
        p_products = paginator.page(paginator.num_pages)

    return render(request,'shop/product/product.html',locals())

#顯示產品細節
def show_product(request, product_id):      #product.html中的{% url "product-url" product.id %} --> 對應到urls --> urls再向此視圖函數發出request
    product = get_object_or_404(models.Product, id=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/product_info.html', locals())
