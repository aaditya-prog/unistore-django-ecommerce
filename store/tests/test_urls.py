from django.test import SimpleTestCase
from django.urls import resolve, reverse

from store.views import *


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("store:index")
        self.assertEquals(resolve(url).func, index)

    def test_order_now_url(self):
        url = reverse("store:order-now")
        self.assertEquals(resolve(url).func, order_now)

    def test_cart_url(self):
        url = reverse("store:cart")
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_checkout_url(self):
        url = reverse("store:checkout")
        self.assertEquals(resolve(url).func, checkout)

    def test_remove_from_cart_url(self):
        url = reverse("store:remove", args=["1"])
        self.assertEquals(resolve(url).func, delete_cart)

    def test_modify_cart_url(self):
        url = reverse("store:modify", args=["1"])
        self.assertEquals(resolve(url).func, modify_cart)
