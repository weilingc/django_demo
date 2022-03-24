from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sku = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(null=True)
    # image = FilerImageField(related_name='product_image',on_delete=models.DO_NOTHING)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits = 8, decimal_places = 0) 

    def __str__(self):
        return self.name
