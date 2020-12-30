from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25, null=False)
    number_of_carts = models.IntegerField(default=0, null=True, blank=True)


class Tags(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    status = (('Pending' , 'Pending'),
        ('Delivered' , 'Delivered'),
        ('Out for delivery', 'Out for delivery'))


    total_price = models.CharField(max_length=150, null=True, blank=True, default=0.0)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length = 50, null=False, default=False, blank=True, choices=status)
    is_empty = models.BooleanField(null=False, default=False, blank=True)
    tags = models.ManyToManyField(Tags)

class HouseHold(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/images/' + self.image


class Groceries(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/images/' + self.image


class Personal_Care(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/images/' + self.image


class Beverages(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/images/' + self.image


class Packaged_Foods(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/images/' + self.image


class Location(models.Model):
    country = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.country

        



class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

class Customer_Location(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)



class Customer_Carts(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)

class Cart_Products(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    beverages_id = models.ForeignKey(Beverages, on_delete=models.CASCADE, null=True, blank=True)
    groceries_id = models.ForeignKey(Groceries, on_delete=models.CASCADE, null=True, blank=True)
    personal_care_id = models.ForeignKey(Personal_Care, on_delete=models.CASCADE, null=True, blank=True)
    household_id = models.ForeignKey(HouseHold, on_delete=models.CASCADE, null=True, blank=True)
    packaged_foods_id = models.ForeignKey(Packaged_Foods, on_delete=models.CASCADE, null=True, blank=True)



