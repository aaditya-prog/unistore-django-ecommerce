from django.core.validators import URLValidator
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="images/blogs")
    description = HTMLField(blank=True, null=True)
    url = models.TextField(validators=[URLValidator()])

    def get_all_blogs():
        return Blog.objects.all()
