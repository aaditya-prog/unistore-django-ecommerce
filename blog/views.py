from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Blog


# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by("id")
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/index.html", {"page_obj": page_obj})
