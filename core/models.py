from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)


class CartItem(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    cart_items = models.ManyToManyField(to=CartItem, blank=True)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(to=CartItem, blank=True)
    total_price = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)