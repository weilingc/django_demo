from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='shop-url'),
    path('shop/<int:category_id>/', views.sort_by_category, name='category-url'), #對應header.html中的 {% url 'category-url' cate.id %}
    path('product/<int:product_id>', views.show_product, name='product-url'),   #對應product.html中的 {% url "product-url" product.id %}
]
