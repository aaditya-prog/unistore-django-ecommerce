from ctypes import resize
from django.db import models
from django.forms import ImageField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()    

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def get_all_products():
        return Product.objects.all()

    def get_products_by_Categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()  