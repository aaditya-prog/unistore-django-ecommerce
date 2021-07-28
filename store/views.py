from django.shortcuts import render, redirect
from .models import Product, Category
from django.views import View
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
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
        products = Product.get_all_products().order_by("id")
    paginator = Paginator(products,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    
    data={}
    data["products"] = products
    data["categories"] = categories
    data["myFilter"] = myFilter
    data["page_obj"] = page_obj
    return render(request, "store/index.html",data)

def checkout(request):
    #use this insdead of print functions in order to test request data.
    from pdb import set_trace
    set_trace()
    return render(request, "checkout/index.html")

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action:", action)
    print("productId", productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    return JsonResponse('Item was added', safe=False) 