from django.shortcuts import render, redirect
from .models import Product, Category
from django.views import View
# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart 
        print(request.session['cart']) 
        return redirect("store:index")
        
            
    def get(self, request):
        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_products_by_Categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data["products"] = products
        data["categories"] = categories
        return render(request, "store/index.html", data)

   