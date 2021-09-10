import os
import os.path
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from mixer.backend.django import mixer

from staff.forms import BlogForm, CategoryForm, ProductForm


class TestForms(TestCase):
    def test_product_form_valid_data(self):
        obj = mixer.blend("store.category")  # creating a fake category object
        from io import BytesIO

        img = BytesIO(b"mybinarydata")
        img.name = "image.jpg"
        form = ProductForm(
            data={
                "name": "Razer Blade 15",
                "price": 500,
                "image": img,
                # creating a mock file for image
                "category": obj.id,
            }
        )
        print("Errors from product form", form.errors)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_data(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_category_form_valid_data(self):
        form = CategoryForm(
            data={
                "name": "Desktops",
            }
        )
        self.assertTrue(form.is_valid())

    def test_category_form_invalid_data(self):
        form = CategoryForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_blog_form_valid_data(self):
        # image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        # print(image)
        image = open(settings.TEST_IMAGE, "rb")
        form = BlogForm(
            data={
                "title": "Blog Title",
                "description": "Blog Description",
                "date": "2021-11-11 11:45",
                "image": image,
                "url": "https://medium.com",
            }
        )
        print(form.fields)
        print("Errors from blog form", form.errors)
        self.assertTrue(form.is_valid())

    def test_blog_form_invalid_data(self):
        form = BlogForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
