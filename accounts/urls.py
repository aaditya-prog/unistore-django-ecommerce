from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("contact", views.contact, name="contact"),
    path("activate-user/<uidb64>/<token>", views.activate_user, name="activate"),
]
