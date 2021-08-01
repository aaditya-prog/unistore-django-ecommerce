from unicodedata import category
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from . forms import RegisterForm, ContactForm
from . models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .decorators import login_excluded, admin_access
from store.models import Product, Category
from blog.models import Blog
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def index(request):
    products = None
        # request.session.get('cart').clear()
    # products = Product.objects.filter(category="Desktop")[:4]
    blogs = Blog.objects.all()[:2]
    data = {}
    # data["products"] = products
    # data["category"] = category
    data["blogs"] = blogs
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

@login_excluded("accounts:index")
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Help form"
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['aadietya.me.d@gmail.com'])
            except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            return redirect ("home:index")
    form = ContactForm()
    return render(request, "contacts/index.html", {"form":form})