import tempfile

from django.test import Client, TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from accounts.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()  # creating a client object for sending requests
        self.client.login(username="aaditya@gmail.com", password="pass1232")
        self.test_user = User.objects.create_user("blah@blah.com", "testpassword")
        self.test_user.is_active = True
        self.test_user.save()

        # setting up urls for the respective views
        self.user_add_url = reverse("staff:useradd")
        self.user_read_url = reverse("staff:userread")
        self.user_delete_url = reverse("staff:delete", args="2")
        self.user_update_url = reverse("staff:update", args="2")

        self.category_add_url = reverse("staff:categoryadd")
        self.category_read_url = reverse("staff:categoryread")
        self.category_delete_url = reverse("staff:deletecategory", args="2")
        self.category_update_url = reverse("staff:deletecategory", args="2")

        self.product_add_url = reverse("staff:productadd")
        self.product_read_url = reverse("staff:productread")
        self.product_delete_url = reverse("staff:deleteproduct", args="2")
        self.product_update_url = reverse("staff:updateproduct", args="2")

        self.blog_add_url = reverse("staff:blogadd")
        self.blog_read_url = reverse("staff:blogread")
        self.blog_delete_url = reverse("staff:deleteblog", args="2")
        self.blog_update_url = reverse("staff:updateblog", args="2")

    # testing CRUD views for users
    def test_user_add(self):
        response = self.client.get(self.user_add_url)
        if self.test_user.is_admin:
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, "admin/users/add.html")
        self.assertEquals(response.status_code, 302)

    def test_user_add_POST(self):
        data = {
            "full_name": "Aaditya Dulal",
            "email": "aadietya.me.d@gmail.com",
            "password": "aaditya",
            "is_staff": 1,
        }
        response = self.client.post(self.user_add_url, data)
        if self.test_user.is_admin:
            self.assertEquals(response.status_code, 200)
            self.assertEquals(data["full_name"], "Aaditya Dulal")
            self.assertTemplateUsed(response, "admin/users/add.html")
        self.assertEquals(response.status_code, 302)

    def test_user_read_GET(self):
        response = self.client.get(self.user_read_url)
        if self.test_user.is_admin:
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, "admin/users/users.html")
        self.assertEquals(response.status_code, 302)

    def test_user_delete(self):
        response = self.client.get(self.user_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_user_update(self):
        response = self.client.get(self.user_update_url)
        self.assertEquals(response.status_code, 302)

    # testing CRUD views for categories
    def test_category_add(self):
        response = self.client.get(self.category_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/category/categoryadd.html")

    def test_category_add_POST(self):
        data = {
            "name": "Laptops",
        }
        response = self.client.post(self.category_add_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data["name"], "Laptops")
        self.assertTemplateUsed(response, "admin/category/categoryadd.html")

    def test_category_read_GET(self):
        response = self.client.get(self.category_read_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/category/categoryread.html")

    def test_category_delete(self):
        response = self.client.get(self.category_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_category_update(self):
        response = self.client.get(self.category_update_url)
        self.assertEquals(response.status_code, 302)

    # testing CRUD views for products
    def test_product_add(self):
        response = self.client.get(self.product_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/product/productadd.html")

    def test_product_add_POST(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        data = {
            "name": "Acer",
            "price": 200,
            "image": image,
            "category": 1,
        }
        response = self.client.post(self.product_add_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data["price"], 200)
        self.assertTemplateUsed(response, "admin/product/productadd.html")

    def test_product_read_GET(self):
        response = self.client.get(self.product_read_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/product/productread.html")

    def test_product_delete(self):
        response = self.client.get(self.product_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_product_update(self):
        response = self.client.get(self.product_update_url)
        self.assertEquals(response.status_code, 302)

    # testing CRUD views for blogs
    def test_blogs_add(self):
        response = self.client.get(self.blog_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/blog/blogadd.html")

    def test_blogs_add_POST(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        data = {
            "name": "Acer",
            "price": 200,
            "image": image,
            "category": 1,
        }
        response = self.client.post(self.blog_add_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data["price"], 200)
        self.assertTemplateUsed(response, "admin/blog/blogadd.html")

    def test_blog_read_GET(self):
        response = self.client.get(self.blog_read_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/blog/blogread.html")

    def test_blog_delete(self):
        response = self.client.get(self.blog_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_blog_update(self):
        response = self.client.get(self.blog_update_url)
        self.assertEquals(response.status_code, 302)
