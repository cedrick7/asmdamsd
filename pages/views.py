# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request, *args, **kwargs):
    # request.user --> @everyone
    # return HttpResponse("<h1>Login</h1>")
    # brauche alle jobs in einer liste, die dann ausgegeben werden können:
        # z.B.: cashier, admin, analyst
    # dann alle user, damit die sich einloggen können --> login-formular
    return render(request, "login.html", {})

def register_view(request, *args, **kwargs):
    # request.user --> @everyone
    return render(request, "register.html", {})

def forgot_password_view(request, *args, **kwargs):
    # request.user --> @everyone
    return render(request, "forgot_password.html", {})

def cashbox_dashboard_view(request, *args, **kwargs):
    # request.user --> @kassierer only!
        # request.user.is_authenticated == true ?
    # return HttpResponse("<h1>Kassierer Dashboard</h1>")
    return render(request, "cashbox_dashboard.html", {})

def cashbox_pay_view(request, *args, **kwargs):
    # request.user --> @kassierer only!
        # request.user.is_authenticated == true ?
    return render(request, "cashbox_pay.html", {})

def admin_dashboard_view(request, *args, **kwargs):
    # request.user --> @admin only!
        # request.user.is_authenticated == true ?
    # return HttpResponse("<h1>Admin Dashboard</h1>")
    return render(request, "admin_dashboard.html", {})

def analyst_dashboard_view(request, *args, **kwargs):
    # request.user --> @analyst only!
        # request.user.is_authenticated == true ?
    # return HttpResponse("<h1>Analyst Dashboard</h1>")
    return render(request, "analyst_dashboard.html", {})