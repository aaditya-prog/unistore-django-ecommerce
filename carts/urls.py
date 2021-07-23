from django.urls import path
from .views import CartView


app_name = "carts"
urlpatterns = [
    path("", CartView.as_view() ,name="index")
]
