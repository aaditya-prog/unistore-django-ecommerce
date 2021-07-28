from django.urls import path
from .views import index
from store import views


app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("checkout", views.checkout, name="checkout"),
    path("update-item", views.updateItem, name="update-item"),

    
]
