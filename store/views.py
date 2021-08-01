from django.contrib import messages
from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Product, Category, Cart
=======
from .models import Product, Category, Product_bought
>>>>>>> origin/main
from django.views import View
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
import json
<<<<<<< HEAD
from .forms import OrderForm
=======

>>>>>>> origin/main

# Create your views here.
def index(request):
    products = None
    # request.session.get('cart').clear()
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    sort = request.GET.get('sort')
    if category_id:
        products = Product.get_products_by_Categoryid(category_id)
    elif sort:
        products = Product.objects.filter().order_by(sort)
    else:
        products = Product.get_all_products().order_by("id")
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
<<<<<<< HEAD
    cart = Cart.objects.filter(is_bought=False)
=======
    cart = Product_bought.objects.filter(is_bought=False)
>>>>>>> origin/main

    data = {"products": products, "categories": categories, "my_filter": my_filter, "page_obj": page_obj,
            "cart": cart}
    return render(request, "store/index.html", data)


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("productId")
        product = Product.objects.get(id=product_id)
        bought_by = request.user
<<<<<<< HEAD
        product_bought = Cart(bought_by=bought_by, product=product)
=======
        product_bought = Product_bought(bought_by=bought_by, product=product)
>>>>>>> origin/main
        product_bought.save()
    return redirect("store:index")


# def add_to_cart(request):
#     if request.method == "POST":
#         product_id = request.POST.get("productId")
#         user_id = request.POST.get("userId")
#         product = Product.objects.get(id=product_id)
#         user = User.objects.get(id=user_id)
#         bought_by = user
#         product_bought = Product_bought(bought_by=bought_by, product=product)
#         product_bought.save()
#         success = "added to cart"
#         return HttpResponse(success)

def delete_cart(request, id):
    if request.method == "POST":
<<<<<<< HEAD
        data = Cart.objects.get(pk=id)
=======
        data = Product_bought.objects.get(pk=id)
>>>>>>> origin/main
        data.delete()
        messages.success(request, "Product successfully deleted.")
    return redirect("store:index")


def checkout(request):
<<<<<<< HEAD
    form = OrderForm()
    items = Cart.objects.filter(is_bought=False).order_by("id")
=======

    items = Product_bought.objects.filter(is_bought=False)
>>>>>>> origin/main
    paginator = Paginator(items, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total = 0
    for item in items:
        total = total + int(item.product.price)
    data = {"page_obj": page_obj,
<<<<<<< HEAD
            "total": total,
            "form": form
            }
    return render(request, "checkout/index.html", data)


def order(request):
    if request.method == "POST":
        pass
    return render(request, "store/index.html")
=======
            "total": total
            }
    return render(request, "checkout/index.html", data)
>>>>>>> origin/main
