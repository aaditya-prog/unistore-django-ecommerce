from django.urls import path
from .views import index
from store import views


app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.add_to_cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("remove/<int:id>", views.delete_cart, name="remove"),
]
