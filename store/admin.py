from django.contrib import admin
from .models import Product, Category
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "image", "category",)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)