from django.test import SimpleTestCase
from django.urls import resolve, reverse

from staff.views import *


class TestUrls(SimpleTestCase):
    def test_logout_url(self):
        url = reverse("staff:logout")
        self.assertEquals(resolve(url).func, logout)

    def test_add_user_url(self):
        url = reverse("staff:useradd")
        self.assertEquals(resolve(url).func, useradd)

    def test_view_users_url(self):
        url = reverse("staff:userread")
        self.assertEquals(resolve(url).func, view_users)

    def test_delete_user_url(self):
        url = reverse("staff:delete", args=["1"])
        self.assertEquals(resolve(url).func, delete_user)

    def test_update_user_url(self):
        url = reverse("staff:update", args=["1"])
        self.assertEquals(resolve(url).func, update_user)

    def test_add_product_url(self):
        url = reverse("staff:productadd")
        self.assertEquals(resolve(url).func, productAdd)

    def test_view_products_url(self):
        url = reverse("staff:productread")
        self.assertEquals(resolve(url).func, ProductView)

    def test_delete_product_url(self):
        url = reverse("staff:deleteproduct", args=["1"])
        self.assertEquals(resolve(url).func, delete_product)

    def test_update_product_url(self):
        url = reverse("staff:updateproduct", args=["1"])
        self.assertEquals(resolve(url).func, update_product)

    def test_add_category_url(self):
        url = reverse("staff:categoryadd")
        self.assertEquals(resolve(url).func, categoryAdd)

    def test_view_categories_url(self):
        url = reverse("staff:categoryread")
        self.assertEquals(resolve(url).func, categoryRead)

    def test_delete_categories_url(self):
        url = reverse("staff:deletecategory", args=["1"])
        self.assertEquals(resolve(url).func, delete_category)

    def test_update_category_url(self):
        url = reverse("staff:categoryupdate", args=["1"])
        self.assertEquals(resolve(url).func, update_category)

    def test_add_blog_url(self):
        url = reverse("staff:blogadd")
        self.assertEquals(resolve(url).func, BlogAdd)

    def test_view_blogs_url(self):
        url = reverse("staff:blogread")
        self.assertEquals(resolve(url).func, BlogView)

    def test_delete_blog_url(self):
        url = reverse("staff:deleteblog", args=["1"])
        self.assertEquals(resolve(url).func, delete_blog)

    def test_update_blog_url(self):
        url = reverse("staff:updateblog", args=["1"])
        self.assertEquals(resolve(url).func, update_blog)

    def test_view_orders_url(self):
        url = reverse("staff:orderread")
        self.assertEquals(resolve(url).func, Order)
