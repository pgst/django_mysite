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

    @property
    def total_price(self):
        return self.item.price * self.quantity


class Cart(models.Model):
    cart_items = models.ManyToManyField(to=CartItem, blank=True)

    def add_cart_item(self, new_cart_item):
        if new_cart_item in [cart_items.item for cart_items in self.cart_items.all()]:
            original_cart_item = self.cart_items.get(
                item_id=new_cart_item.item.id)
            original_cart_item.quantity += new_cart_item.quantity
            original_cart_item.save()
        else:
            new_cart_item.save()
            self.cart_items.add(new_cart_item)

    @property
    def total_price(self):
        return sum([cart_item.total_price for cart_item in self.cart_items.all()])


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(to=CartItem, blank=True)
    order_price = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
