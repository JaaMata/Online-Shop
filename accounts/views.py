from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dashboard.models import *


# Create your views here.

def account(request, id):
    if request.user.id == id:
        user = request.user
        customer = Customer.objects.get(user=user)
        orders = Order.objects.all()
        orders = orders.filter(customer=customer)

        context = {"orders" : orders}
        return render(request, "account.html", context)
    else:
        return render(request, "404.html")
