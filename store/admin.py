from django.contrib import admin

from .models import Cart, Category, Orders, Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "image", "category")


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Orders)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "receiver",
        "phone",
        "email",
        "city",
        "street",
        "building",
        "payment",
        "promo",
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "bought_by", "product", "quantity", "is_bought")
