from django.test import TestCase

from accounts.forms import LoginForm, RegisterForm


class TestForms(TestCase):
    def test_register_form_valid_data(self):
        form = RegisterForm(
            data={
                "full_name": "Aaditya Dulal",
                "email": "aadietya.me.d@gmail.com",
                "password": "validated",
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_form_invalid_data(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_user_add_form_valid_data(self):
        form = RegisterForm(
            data={
                "full_name": "Aaditya Dulal",
                "email": "aadietya.me.d@gmail.com",
                "password": "validated",
                "staff": 0,
            }
        )
        self.assertTrue(form.is_valid())

    def test_user_add_form_invalid_data(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(
            len(form.errors), 3
        )  # As "staff" is an optional field, error message is not generated.

    def test_login_form_invalid_data(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
