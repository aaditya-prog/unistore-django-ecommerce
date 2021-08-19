from django import forms
from tinymce.widgets import TinyMCE
from store.models import Product, Category
from blog.models import Blog


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "image", "category"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-group form-control w-25 p-3",
                    "Placeholder": "Enter product name",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-group form-control w-25 p-3",
                    "Placeholder": "Enter quantity",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-group form-control-file",
                    "Placeholder": "Upload Image",
                }
            ),
        }

        error_messages = {
            "name": {"required": "You must provide the product's name"},
            "price": {"required": "Price must be mentioned"},
            "image": {"required": "Error: image required"},
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description", "date", "image", "url"]
        widgets = {
            "title": forms.TextInput(),
            "description": TinyMCE(attrs={"required": False, "cols": 30, "rows": 10}),
            "date": forms.DateTimeInput(),
            "image": forms.FileInput(),
            "url": forms.TextInput(),
        }

        error_messages = {
            "title": {"required": "You must provide the blog title"},
            "image": {"required": "Error: image required"},
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-group form-control w-25 p-3",
                    "Placeholder": "Enter category name",
                }
            )
        }

        error_messages = {"name": {"required": "You must provide the Category's name"}}
