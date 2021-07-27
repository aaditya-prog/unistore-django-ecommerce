from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . forms import RegisterForm, UserAddForm
from . models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .decorators import login_excluded, admin_access
from store.models import Product, Category
# Create your views here.
def index(request):
    products = None
        # request.session.get('cart').clear()
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category = Category.category_id).order_by("-id")[:1]
    else:
        products = Product.objects.filter().order_by("-id")[:1]

    data = {}
    data["products"] = products
    data["categories"] = categories
    return render(request, "home/index.html",data)

def register(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["full_name"]
            email = fm.cleaned_data['email']
            password = fm.cleaned_data["password"]
            user = User(full_name=name, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(
                request, "User registration Successful"
            )
        else:
            messages.error(request, "Registration failed")   
    else:
        fm = RegisterForm() 
    return render(request, "home/register.html", {"form":fm})

@login_excluded("home:index")
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            un = fm.cleaned_data["username"]
            pw = fm.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                if user.admin:
                    return redirect("staff:userread")
                if not user.admin:    
                    return redirect("home:index")
              
    else:
        fm = AuthenticationForm()
    return render(request, "home/login.html", {"form": fm})

def user_logout(request):
    logout(request)
    return redirect("home:index")

