from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Blog


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()  # creating a client object for sending requests

        # setting up urls for the index view
        self.index_url = reverse("blog:index")

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")
