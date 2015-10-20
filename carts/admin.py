from django.contrib import admin

from .models import Cart, CartItem


class CartItemInLine(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInLine,
    ]

    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
