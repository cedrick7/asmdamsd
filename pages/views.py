# from django.http import HttpResponse
from django.shortcuts import render

# -------------------------------------------------------------------------
# login and similar

# who can access:
    # --> eveyone
# what i need:
    # a list of all the jobs (cashier, admin, analyst)
    # login-data to check wether the input is correct or not

def auth_login_view(request, *args, **kwargs):
    return render(request, "auth_login.html", {})

def auth_register_view(request, *args, **kwargs):
    return render(request, "auth_register.html", {})

def auth_forgot_password_view(request, *args, **kwargs):
    return render(request, "auth_forgot_password.html", {})

def auth_change_password_view(request, *args, **kwargs):
    return render(request, "auth_change_password.html", {})


# -------------------------------------------------------------------------
# everyone

# who can access:
    # costumer --> cashier and admin
    # profile --> eveyone
# what i need:
    # a list of all the costumers and their information
    # profile information

def all_costumer_view(request, *args, **kwargs):
    return render(request, "all_costumer.html", {})

def all_profile_view(request, *args, **kwargs):
    return render(request, "all_profile.html", {})


# -------------------------------------------------------------------------
# cashier

# who can access:
    # --> cashier only
# what i need:
    # a list of all the products + services
    # a list of all categories
    # a list of all the payment-options

def cashbox_dashboard_view(request, *args, **kwargs):
    return render(request, "cashbox_dashboard.html", {})

def cashbox_pay_view(request, *args, **kwargs):
    return render(request, "cashbox_pay.html", {})

def cashbox_more_view(request, *args, **kwargs):
    return render(request, "cashbox_more.html", {})


# -------------------------------------------------------------------------
# admin

# who can access:
    # --> admin only
# what i need:
    # a list of all the products
    # a list of all the services
    # a list of all the categories
    # a list of all the attributes
    # a list of all the discounts
    # a list of all the employees with their information
    # a list of all the invoices with their information
    # a list of all the cashboxes and their online/offline-status + money in there
    # a list of all the safes and their online/offline-status + money in there
    # a list of all the backups with their information
    # a list of all the payment-options
    # a list of all the requests + a way to handle them


def admin_dashboard_view(request, *args, **kwargs):
    return render(request, "admin_dashboard.html", {})

def admin_products_view(request, *args, **kwargs):
    return render(request, "admin_products.html", {})

def admin_products_detail_view(request, *args, **kwargs):
    return render(request, "admin_products_detail.html", {})

def admin_services_view(request, *args, **kwargs):
    return render(request, "admin_services.html", {})

def admin_services_detail_view(request, *args, **kwargs):
    return render(request, "admin_services_detail.html", {})

def admin_categories_view(request, *args, **kwargs):
    return render(request, "admin_categories.html", {})

def admin_categories_detail_view(request, *args, **kwargs):
    return render(request, "admin_categories_detail.html", {})

def admin_attributes_view(request, *args, **kwargs):
    return render(request, "admin_attributes.html", {})

def admin_attributes_detail_view(request, *args, **kwargs):
    return render(request, "admin_attributes_detail.html", {})

def admin_discounts_view(request, *args, **kwargs):
    return render(request, "admin_discounts.html", {})

def admin_discounts_detail_view(request, *args, **kwargs):
    return render(request, "admin_discounts_detail.html", {})

def admin_employees_view(request, *args, **kwargs):
    return render(request, "admin_employees.html", {})

def admin_employees_detail_view(request, *args, **kwargs):
    return render(request, "admin_employees_detail.html", {})

def admin_invoices_view(request, *args, **kwargs):
    return render(request, "admin_invoices.html", {})

def admin_invoices_detail_view(request, *args, **kwargs):
    return render(request, "admin_invoices_detail.html", {})

def admin_cashboxes_view(request, *args, **kwargs):
    return render(request, "admin_cashboxes.html", {})

def admin_safes_view(request, *args, **kwargs):
    return render(request, "admin_safes.html", {})

def admin_backups_view(request, *args, **kwargs):
    return render(request, "admin_backups.html", {})

def admin_backups_detail_view(request, *args, **kwargs):
    return render(request, "admin_backups_detail.html", {})

def admin_payments_view(request, *args, **kwargs):
    return render(request, "admin_payments.html", {})

def admin_requests_view(request, *args, **kwargs):
    return render(request, "admin_requests.html", {})


# -------------------------------------------------------------------------
# analyst

# who can access:
    # --> analyst only
# what i need:
    # a list of all the

def analyst_dashboard_view(request, *args, **kwargs):
    return render(request, "analyst_dashboard.html", {})

def analyst_sales_view(request, *args, **kwargs):
    return render(request, "analyst_sales.html", {})

def analyst_costumers_view(request, *args, **kwargs):
    return render(request, "analyst_costumers.html", {})

def analyst_employees_view(request, *args, **kwargs):
    return render(request, "analyst_employees.html", {})
