from decimal import Decimal
from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from carts.models import Cart


class UserCheckout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


ADDRESS_TYPE = (
    ("billing", "Billing"),
    ("shipping", "Shipping"),
)


class UserAddress(models.Model):
    user = models.ForeignKey(UserCheckout)
    type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    county = models.CharField(max_length=120)
    postcode = models.CharField(max_length=120)

    def __str__(self):
        return self.street

    def get_address(self):
        return "%s, %s, %s %s" %(self.street, self.city, self.county, self.postcode)


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('completed', 'Completed')
)



class Order(models.Model):
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
    cart = models.ForeignKey(Cart)
    user = models.ForeignKey(UserCheckout, null=True)
    billing_address = models.ForeignKey(UserAddress, related_name='billing_address', null=True)
    shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address', null=True)
    shipping_total_price = models.DecimalField(decimal_places=2, max_digits=50, default=0.0)
    order_total = models.DecimalField(decimal_places=2, max_digits=50, default=0.0)
    order_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.cart.id)

    def mark_completed(self):
        self.status = "completed"
        self.save()


def order_pre_save(sender, instance, *args, **kwargs):
    shipping_total_price = instance.shipping_total_price
    cart_total = instance.cart.total
    order_total = Decimal(shipping_total_price) + Decimal(cart_total)
    instance.order_total = order_total

pre_save.connect(order_pre_save,sender=Order)