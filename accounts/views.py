from unicodedata import category

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.shortcuts import HttpResponse, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import (DjangoUnicodeDecodeError, force_bytes,
                                   force_str, force_text)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from blog.models import Blog
from store.models import Product

from .decorators import login_excluded
from .forms import ContactForm, LoginForm, RegisterForm
from .models import User
from .utils import generate_token


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


# function to send an activation email
def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Complete your registration"
    email_body = render_to_string(
        "accounts/activate.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(subject=email_subject, body=email_body, to=[user.email])

    email.send()


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Email verified, login to continue.")
        return redirect(reverse("accounts:login"))
    else:
        return render(request, "accounts/activate-failed.html", {"user": user})


def index(request):
    # products = None
    # request.session.get('cart').clear()
    # products = Product.objects.filter(category="Desktop")[:4]
    blogs = Blog.objects.all()[:2]
    desktops = Product.objects.filter(category=1).order_by("-id")[:4]
    laptops = Product.objects.filter(category=2).order_by("-id")[:4]
    hybrids = Product.objects.filter(category=3).order_by("-id")[:3]
    tablets = Product.objects.filter(category=4).order_by("-id")[:4]
    context = {
        "blogs": blogs,
        "desktops": desktops,
        "laptops": laptops,
        "tablets": tablets,
        "hybrids": hybrids,
    }
    # data["products"] = products
    # data["category"] = category

    return render(request, "home/index.html", context)


@login_excluded("accounts:index")
def register(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["full_name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            if len(name) < 3:
                messages.error(request, "Invalid name, try again.")
            elif has_numbers(name):
                messages.error(request, "Numbers are not allowed in names.")
            elif len(password) < 8:
                messages.error(
                    request, "Your password must contain more than 8 characters."
                )
            elif not has_numbers(password):
                messages.error(request, "Your password must contain a numeric value.")
            else:
                user = User(full_name=name, email=email, password=password)
                user.is_active = False
                user.set_password(password)
                user.save()
                send_activation_email(user, request)
                messages.success(
                    request, "Registration Successful, verify your email to login."
                )
        else:
            messages.error(request, "Registration failed, try again.")
    else:
        fm = RegisterForm()
    return render(request, "home/register.html", {"form": fm})


@login_excluded("accounts:index")
def user_login(request):
    if request.method == "POST":
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            un = fm.cleaned_data["username"]
            pw = fm.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                request.session["user_id"] = user.id
                request.session["user_email"] = user.email
                if user.admin:
                    return redirect("staff:userread")
                if not user.admin:
                    return redirect("accounts:index")

    else:
        fm = LoginForm()
    return render(request, "home/login.html", {"form": fm})


def user_logout(request):
    logout(request)
    return redirect("accounts:index")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Help form"
            from_email = form.cleaned_data["email_address"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["aadietya.me.d@gmail.com"])
                messages.success(request, "Message sent.")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("accounts:index")
        else:
            messages.error(request, "Could not send message, try again.")
    form = ContactForm()
    return render(request, "contacts/index.html", {"form": form})
