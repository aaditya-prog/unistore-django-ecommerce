from django.test import SimpleTestCase
from django.urls import resolve, reverse

from accounts.views import (activate_user, contact, index, register,
                            user_login, user_logout)


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("accounts:index")
        self.assertEquals(resolve(url).func, index)

    def test_register_url(self):
        url = reverse("accounts:register")
        self.assertEquals(resolve(url).func, register)

    def test_login(self):
        url = reverse("accounts:login")
        self.assertEquals(resolve(url).func, user_login)

    def test_activate_user_url(self):
        url = reverse("accounts:activate", args=["id", "token"])
        self.assertEquals(resolve(url).func, activate_user)

    def test_logout(self):
        url = reverse("accounts:logout")
        self.assertEquals(resolve(url).func, user_logout)

    def test_contact(self):
        url = reverse("accounts:contact")
        self.assertEquals(resolve(url).func, contact)
