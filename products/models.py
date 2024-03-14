from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    description = models.TextField()
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=60)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name



class Order(models.Model):
    order_items=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    Order_status=models.BooleanField(null=True,default="pending")
    address=models.TextField(null=True)
    price=models.IntegerField(null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.product_name}"
