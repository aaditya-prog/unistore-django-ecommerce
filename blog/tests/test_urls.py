from django.test import SimpleTestCase
from django.urls import resolve, reverse

from blog.views import index


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("blog:index")
        self.assertEquals(resolve(url).func, index)
