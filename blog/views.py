from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    blogs = Blog.get_all_blogs
    return render(request, "blog/index.html", {"blogs": blogs})