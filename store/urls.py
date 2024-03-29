from django.urls import path

from store import views

from .views import index

app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("order-now", views.order_now, name="order-now"),
    path("cart", views.add_to_cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("remove/<int:id>", views.delete_cart, name="remove"),
    path("modify/<int:id>", views.modify_cart, name="modify"),
]
