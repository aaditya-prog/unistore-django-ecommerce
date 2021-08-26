from django.urls import path

from . import views

app_name = "staff"
urlpatterns = [
    path("logout", views.logout, name="logout"),
    path("add-user", views.useradd, name="useradd"),
    path("view-user", views.view_users, name="userread"),
    path("delete-user/<int:id>", views.delete_user, name="delete"),
    path("update-user/<int:id>", views.update_user, name="update"),
    path("add-product", views.productAdd, name="productadd"),
    path("view-product/", views.ProductView, name="productread"),
    path("delete-product/<int:id>", views.delete_product, name="deleteproduct"),
    path("update-product/<int:id>", views.update_product, name="updateproduct"),
    path("add-category", views.categoryAdd, name="categoryadd"),
    path("view-category/", views.categoryRead, name="categoryread"),
    path("delete-category/<int:id>", views.delete_category, name="deletecategory"),
    path("update-category/<int:id>/", views.update_category, name="categoryupdate"),
    path("add-blog", views.BlogAdd, name="blogadd"),
    path("view-blog/", views.BlogView, name="blogread"),
    path("delete-blog/<int:id>", views.delete_blog, name="deleteblog"),
    path("update-blog/<int:id>", views.update_blog, name="updateblog"),
    path("view-orders/", views.Order, name="orderread"),
]
