from django.contrib import admin

from .models import Product, Variation, ProductImage, Category, ProductFeatured


class VariationInline(admin.TabularInline):
    model = Variation


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):

    # choose what to view under product page
    list_display = ["__str__", "price"]
    inlines = [
        ProductImageInline,
        VariationInline,
    ]

    class Meta:
        model = Product

# don't forget to add the new admin class
admin.site.register(Product, ProductAdmin)
# admin.site.register(Variation)
# admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)
