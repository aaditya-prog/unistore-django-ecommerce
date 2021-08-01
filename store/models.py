from django.db import models
from accounts.models import User


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
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()


class Cart(models.Model):
    bought_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_bought = models.BooleanField(default=False)


PAYMENT_CHOICES = [
    ('COD', 'Cash on delivery'),
    ('Paypal', 'Paypal'),
    ('Card', 'Use your credit/debit card'),
]


class Orders(models.Model):
    items = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.IntegerField()
    receiver = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    promo = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

