from django.contrib.auth.models import User  # django自建User模組
from django.db import models

from shop.models import Product


class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    postal_code = models.DecimalField(max_digits=6,decimal_places=0) #郵遞區號最多6碼
    total = models.DecimalField(max_digits=10, decimal_places=0)
    phone = models.DecimalField(max_digits=13, decimal_places=0)
    created_date = models.DateTimeField(auto_now_add=True) #訂單生成時自動產生日期
    
    class Meta:
        ordering = ('created_date',)
    
    def __str__(self):
        return '訂單編號:{}'.format(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    qty = models.PositiveIntegerField(default=1)
