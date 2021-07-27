from django.shortcuts import render, redirect
from .models import Product, Category
from django.views import View
from .filters import ProductFilter 
# Create your views here.
def index(request):
    products = None
    # request.session.get('cart').clear()
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    sort = request.GET.get('sort')
    if categoryID:
        products = Product.get_products_by_Categoryid(categoryID)
    elif sort:
        products = Product.objects.filter().order_by(sort)      
    else:
        products = Product.get_all_products()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    data={}
    data["products"] = products
    data["categories"] = categories
    data["myFilter"] = myFilter
    return render(request, "store/index.html",data)

