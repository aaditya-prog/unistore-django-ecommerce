from django.test import TestCase
from accounts.models import User


class TestModels(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='aaditya@gmail.com')
        user.set_password('premier123')
        user.save()

        self.assertEqual(str(user), 'aaditya@gmail.com')
