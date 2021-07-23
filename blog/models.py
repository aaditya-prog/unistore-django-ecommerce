from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/blogs')
    description = models.TextField()
    url = models.TextField(validators=[URLValidator()])


    def get_all_blogs():
        return Blog.objects.all()