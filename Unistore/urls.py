"""Unistore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.accounts, name='accounts')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='accounts')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

import docs

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include("docs.urls")),
    path("store/", include("store.urls")),
    path("", include("accounts.urls")),
    path("blog/", include("blog.urls")),
    path("staff/", include("staff.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("tinymce/", include("tinymce.urls")),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
