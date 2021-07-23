from django.urls import path
from .views import Index
from store import views


app_name = "store"
urlpatterns = [
    path("", Index.as_view() ,name="index"),
    
]
