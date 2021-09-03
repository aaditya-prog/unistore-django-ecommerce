from django.test import TestCase
from accounts.forms import RegisterForm, LoginForm


class TestForms(TestCase):

    def test_register_form_valid_data(self):
        form = RegisterForm(data={
            'full_name': 'Aaditya Dulal',
            'email': 'aadietya.me.d@gmail.com',
            'password': 'validated'
        })
        self.assertTrue(form.is_valid())

    def test_register_form_invalid_data(self):
        form = RegisterForm(data={

        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username': 'aadityadulal@gmail.com',
            'password': 'premier1232'
        })
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_data(self):
        form = LoginForm(data={

        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
