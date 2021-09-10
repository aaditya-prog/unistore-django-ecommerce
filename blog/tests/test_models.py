from django.test import TestCase
from django.utils import timezone

from blog.models import Blog


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.blog = Blog.objects.create(
            title="Blog Title",
            date="2021-01-10 10:44",
            image="",
            description="The description of blogs",
            url="https://meet.google.com/",
        )

    def test_blog_model_has_information_fields(self):
        self.assertEqual(str(self.blog.title), "Blog Title")
        self.assertEqual(self.blog.date, "2021-01-10 10:44")
        # self.assertEqual(int(self.blog.image), "")
        self.assertEqual(str(self.blog.description), "The description of blogs")
        self.assertEqual(str(self.blog.url), "https://meet.google.com/")
