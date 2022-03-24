from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart-url'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add-url'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove-url'),
]
