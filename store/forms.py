from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["receiver", "phone", "email", "city", "street", "building", "payment", "promo", "user"]
        widgets = {
            "receiver": forms.TextInput(
                attrs={
                    "placeholder": "ID provable name to receive products at the time of delivery",
                    "class": "form-control",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Immediately reachable phone number",
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email where you want to get notified about the orders.",
                    "class": "form-control",
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "street": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "building": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "payment": forms.Select(
                attrs={
                    "class": "form-control",

                }
            ),
        }
