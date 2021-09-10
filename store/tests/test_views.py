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
        self.test_user.is_active = False
        self.test_user.save()

        # setting up urls for the respective views
        self.index_url = reverse("store:index")
        self.add_to_cart_url = reverse("store:cart")
        self.cart_delete_url = reverse("store:remove", args="2")
        self.order_now_url = reverse("store:order-now")
        self.checkout_url = reverse("store:checkout")

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "store/index.html")

    def test_add_to_cart_POST(self):
        data = {
            "product": "Acer",
            "quantity": "1",
            "user": "1",
        }
        response = self.client.post(self.add_to_cart_url, data)
        self.assertEquals(data["user"], "1")
        self.assertEquals(response.status_code, 302)

    def test_cart_delete(self):
        response = self.client.get(self.cart_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_order_now(self):
        data = {
            "product": "Acer",
            "quantity": "1",
            "user": "1",
        }
        response = self.client.post(self.order_now_url, data)
        self.assertEquals(data["user"], "1")
        self.assertEquals(response.status_code, 302)

    def test_checkout_GET(self):
        response = self.client.get(self.checkout_url)
        if self.test_user.is_active:
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, "checkout/index.html")
        self.assertEquals(response.status_code, 302)

    def test_checkout_POST(self):
        data = {
            "receiver": "Receiver",
            "phone": "9808629002",
            "email": "aaditya@gmail.com",
            "city": "KTM",
            "street": "Freak Street",
            "building": "Pepsicola",
            "payment": "COD",
            "promo": "SUMMER",
        }
        response = self.client.post(self.checkout_url, data)
        if self.test_user.is_active:
            self.assertEquals(response.status_code, 200)
            self.assertEquals(data["promo"], "SUMMER")
            self.assertTemplateUsed(response, "checkout/index.html")
        self.assertEquals(response.status_code, 302)
