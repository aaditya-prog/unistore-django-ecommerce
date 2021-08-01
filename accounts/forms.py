from django import forms
from django.forms import ModelForm
from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["full_name", "email", "password", ]

        labels = {
            "full_name": "Full Name",
            "email": "Email",
            "password": "Password",

        }

        # help_text = {
        #     "password": "Include numbers for better security",
        # }

        error_messages = {
            "full_name": {"required": "you must enter your name"},
            "email": {"required": "Email required"},
            "password": {"required": "You must enter your password"},
        }

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your name",
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email",
                    "class": "form-control",
                }
            ),

            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Choose a password",
                    "class": "form-control",
                }
            ),

        }


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["full_name", "email", "password", "staff", ]

        labels = {
            "full_name": "Full Name",
            "email": "Email",
            "password": "Password",
            "staff": "Register as staff",
        }

        # help_text = {
        #     "password": "Include numbers for better security",
        # }

        error_messages = {
            "full_name": {"required": "you must enter your name"},
            "email": {"required": "Email required"},
            "password": {"required": "You must enter your password"},
        }

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your name",
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email",
                    "class": "form-control",
                }
            ),

            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Choose a password",
                    "class": "form-control",
                }
            ),

            "staff": forms.CheckboxInput(
                attrs={
                    "class": "form-check",
                }
            ),
        }


class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    email_address = forms.EmailField(max_length=150)
