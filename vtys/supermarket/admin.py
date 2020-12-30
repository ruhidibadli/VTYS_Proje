from django.contrib import admin
from .models import *
# Register your models here.

models=[
    Customer,
    Tags,
    Cart,
    HouseHold,
    Groceries,
    Personal_Care,
    Beverages,
    Packaged_Foods,
    Location,
    Orders,
    Customer_Location,
    Customer_Carts,
    Cart_Products
]
admin.site.register(models)