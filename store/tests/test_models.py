import tempfile

from django.test import TestCase

from store.models import Category, Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        file_mock = tempfile.NamedTemporaryFile(
            suffix="ad.jpg"
        ).name  # creating a mock image file
        category = Category(name="Laptop")
        category.save()
        product = Product(name="ASUS", price=400, category=category)
        product.save()

        cls.fields = Product.objects.create(name="Name", price="500", image=file_mock)

    def test_product_model_has_fields(self):
        self.assertEqual(str(self.fields.name), "Name")
        self.assertEqual(str(self.fields.price), "500")

    def test_foreign_key_category(self):
        item = Product.objects.get(id=1)
        self.assertEqual(item.category.name, "Laptop")
