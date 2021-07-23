from django.shortcuts import render, HttpResponseRedirect, redirect
from home.forms import UserAddForm, RegisterForm
from home.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from store.models import Category, Product
from .forms import ProductForm, CategoryForm, BlogForm
from blog.models import Blog

# Create your views here.
def useradd(request):
    if request.method == "POST":
        fm = UserAddForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["full_name"]
            email = fm.cleaned_data['email']
            password = fm.cleaned_data["password"]
            staff = fm.cleaned_data["staff"]
            user = User(full_name=name, email=email, password=password, staff=staff)
            user.set_password(password)
            user.save()
            messages.success(
                request, "User registration Successful"
            )
        else:
            messages.error(request, "Registration failed")   
    else:
        fm = UserAddForm() 
    return render(request, "admin/users/add.html", {"form":fm})

def view_users(request):
    userdata = User.objects.all()
    return render(request, "admin/users/users.html", {"userdata": userdata})

def delete_user(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect("/view-user")

def update_user(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        pw = request.POST.copy()
        fm = RegisterForm(pw, instance=data)
        if len(request.POST["password"]) < 4:
            context = {
                "form": fm,
                "error": "Password must be greater than 3",
            }
            return render(request, "admin/users/update.html", context)
        pw["password"] = make_password(request.POST["password"])

        if fm.is_valid():
            fm.save()
            messages.success(request, "User details updated successfully.")
        else:
            messages.error(request, "Update Failed, try again.")
    else:
        data = User.objects.get(pk=id)
        fm = RegisterForm(instance=data)
    return render(request, "admin/users/update.html", {"form": fm})

def logout(request):
    return render(request, "home/index.html")

def productAdd(request):
    if request.method == "POST":
        frm = ProductForm(data=(request.POST or None), files=(request.FILES or None))
        if frm.is_valid():
            nm = frm.cleaned_data["name"]
            pr = frm.cleaned_data["price"]
            ct = frm.cleaned_data["category"]
            img = frm.cleaned_data["image"]
            product = Product(name=nm, price=pr, category= ct, image=img)
            product.save()
            frm = ProductForm()
            messages.success(request, "Product added successfully.")

        else:
            messages.error(request, "Fill the form correctly and try again.")
    else:
        frm = ProductForm()
    return render(request, "admin/product/productadd.html", {"form": frm})


def ProductView(request):
    productdata = Product.objects.all()
    return render(request, "admin/product/productread.html", {"data": productdata})


def delete_product(request, id):
    if request.method == "POST":
        data = Product.objects.get(pk=id)
        data.delete()
        messages.success(request, "Product successfully deleted.")
    return redirect("staff:productread")


def update_product(request, id):
    if request.method == "POST":
        data = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User details updated successfully.")
        else:
            messages.error(request, "Update Failed, try again.")
    else:
        data = Product.objects.get(pk=id)
        fm = ProductForm(instance=data)
    return render(request, "admin/product/productupdate.html", {"form": fm})

def categoryAdd(request):
    if request.method == "POST":
        fm = CategoryForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            data = Category(name=nm)
            data.save()
            messages.success(request, "New Category Added Successfully.")
            fm = CategoryForm()
        else:
            messages.error(
                request, "Category not added, fill in the details correctly."
            )

    else:
        fm = CategoryForm()
    return render(request, "admin/category/categoryadd.html", {"form": fm})


def categoryRead(request):
    data = Category.objects.all()
    return render(request, "admin/category/categoryread.html", {"catdata": data})


def delete_category(request, id):
    if request.method == "POST":
        data = Category.objects.get(pk=id)
        data.delete()
        messages.success(request, "One category deleted successfully")
    return redirect("staff:categoryread")



def update_category(request, id):
    if request.method == "POST":
        data = Category.objects.get(pk=id)
        fm = CategoryForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Category details updated successfully.")
        else:
            messages.error(request, "Update Failed, try again.")
    else:
        data = Category.objects.get(pk=id)
        fm = CategoryForm(instance=data)
    return render(request, "admin/category/categoryupdate.html", {"form": fm})


def BlogAdd(request):
    if request.method == "POST":
        frm = BlogForm(data=(request.POST or None), files=(request.FILES or None))
        if frm.is_valid():
            tt = frm.cleaned_data["title"]
            date = frm.cleaned_data["date"]
            desc = frm.cleaned_data["description"]
            img = frm.cleaned_data["image"]
            url = frm.cleaned_data["url"]
            blog = Blog(title=tt, date=date, description=desc, image=img, url=url)
            blog.save()
            frm = BlogForm()
            messages.success(request, "Blog added successfully.")

        else:
            messages.error(request, "Fill the form correctly and try again.")
    else:
        frm = BlogForm()
    return render(request, "admin/blog/blogadd.html", {"form": frm})


def BlogView(request):
    blogdata = Blog.objects.all()
    return render(request, "admin/blog/blogread.html", {"blogdata": blogdata})


def delete_blog(request, id):
    if request.method == "POST":
        data = Blog.objects.get(pk=id)
        data.delete()
        messages.success(request, "Blog successfully deleted.")
    return redirect("staff:blogread")

def update_blog(request, id):
    if request.method == "POST":
        data = Blog.objects.get(pk=id)
        fm = BlogForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User details updated successfully.")
        else:
            messages.error(request, "Update Failed, try again.")
    else:
        data = Blog.objects.get(pk=id)
        fm = BlogForm(instance=data)
    return render(request, "admin/blog/blogupdate.html", {"form": fm})