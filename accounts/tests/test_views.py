from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User


class TestViews(TestCase):
    client = Client()

    def test_index(self):
        client = Client()
        index_url = reverse("accounts:index")
        response = client.get(index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_register_GET(self):
        register_url = reverse("accounts:register")
        client = Client()
        response = client.get(register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/register.html")

    def test_register_POST(self):
        client = Client()
        register_url = reverse("accounts:register")
        User.objects.create(
            full_name="Aaditya Dulal", email="aadietya.me.d@gmail.com", password="aaditya"
        )
        response = client.post(register_url, {})
        self.assertEquals(response.status_code, 200)
