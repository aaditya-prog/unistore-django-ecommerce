from django.test import TestCase
from mixer.backend.django import mixer

from accounts.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.userdata = mixer.blend(User)

    def test_user_model_has_information_fields(self):
        self.assertIsInstance(self.userdata.email, str)
        self.assertIsInstance(self.userdata.full_name, str)
        self.assertIsInstance(self.userdata.is_active, int)
        self.assertIsInstance(self.userdata.staff, int)
        self.assertIsInstance(self.userdata.admin, int)
        self.assertIsInstance(self.userdata.password, str)
