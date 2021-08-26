from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_index_GET(self):
        client = Client()

        response = client.get(reverse("index"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
