from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create-url'),
    path('order_confirmed/', views.order_confirmed, name='order_confirmed-url'),
    path('myorders/', views.myorders, name='myorders-url'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail-url'),
]
