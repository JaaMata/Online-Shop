from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *



# Create your views here.

def home(request):
    return render(request, "home.html")


def dashboard(request):
    orders = Order.objects.all()
    deliveredOrders = orders.filter(status="Delivered").count()
    pending = orders.filter(status='Pending').count()
    totalOrders = orders.count()
    userId = request.user.id

    context = {"orders": orders, "deliveredOrders": deliveredOrders, "totalOrders": totalOrders ,"pendingOrders":pending, "userId" : userId}
    return render(request, "dashboard.html", context)


def products(request):
    return render(request, "products.html")

