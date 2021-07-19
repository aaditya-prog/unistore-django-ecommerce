from django.urls import path
from blog import views


app_name = "users"
urlpatterns = [
    path("", views.index ,name="index")
]
