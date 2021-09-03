from django.test import SimpleTestCase
from django.urls import resolve, reverse

from accounts.views import activate_user, index, register


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("accounts:index")
        self.assertEquals(resolve(url).func, index)

    def test_register_url(self):
        url = reverse("accounts:register")
        self.assertEquals(resolve(url).func, register)

    def test_activate_user_url(self):
        url = reverse("accounts:activate", args=["id", "token"])
        self.assertEquals(resolve(url).func, activate_user)
