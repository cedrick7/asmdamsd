"""Projekt1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import login_view, register_view, forgot_password_view,\
                        cashbox_dashboard_view, cashbox_pay_view, costumer_view, profile_view,\
                        admin_dashboard_view, analyst_dashboard_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('kasse/', cashbox_dashboard_view, name='cashbox_dashboard'),
    path('pay/', cashbox_pay_view, name='pay'),
    path('costumer/', costumer_view, name='costumer'),
    path('profile/', profile_view, name='profile'),
    path('admin/', admin_dashboard_view, name='admin_dashboard'),
    path('analyst/', analyst_dashboard_view, name='analyst_dashboard'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
