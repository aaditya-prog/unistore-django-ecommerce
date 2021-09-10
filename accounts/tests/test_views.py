from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()  # creating a client object for sending requests

        # setting up urls for the respective views
        self.index_url = reverse("accounts:index")
        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:login")
        self.contact_url = reverse("accounts:contact")

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    #  for registration process
    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/register.html")

    def test_register_POST(self):
        data = {
            "full_name": "Aaditya Dulal",
            "email": "aadietya.me.d@gmail.com",
            "password": "aaditya",
        }
        response = self.client.post(self.register_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data["full_name"], "Aaditya Dulal")

    # for login process
    def test_login_GET(self):

        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/login.html")

    def test_login_POST(self):
        data = {"email": "aadietya.me.d@gmail.com", "password": "aaditya"}
        response = self.client.post(self.login_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data["password"], "aaditya")

    def test_login_authentication(self):
        self.client.login(username="aaditya@gmail.com", password="pass1232")
        response = self.client.post(self.login_url)
        self.assertEquals(response.status_code, 200)

    # for contact
    def test_contact_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts/index.html")

    def test_contact_POST(self):
        data = {
            "email_address": "aadietya.me.d@gmail.com",
            "message": "This is a message.",
        }
        response = self.client.post(self.contact_url, data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(data["email_address"], "aadietya.me.d@gmail.com")
