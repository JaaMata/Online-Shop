from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tag_name


class Product(models.Model):
    name = models.CharField(null=True, max_length=200)
    price = models.FloatField(null=True)
    description = models.CharField(null=True, max_length=200)
    img = models.ImageField(upload_to="product-img", null=True)
    tag = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return "Order for " + self.customer.name
