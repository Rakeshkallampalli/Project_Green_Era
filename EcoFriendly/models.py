from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    eco_certification = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.CharField(max_length=100)
    material = models.CharField(max_length=255)
    manufacturing_location = models.CharField(max_length=255)
    packaging_type = models.CharField(max_length=255)
    recyclable = models.BooleanField(default=False)
    biodegradable = models.BooleanField(default=False)
    cruelty_free = models.BooleanField(default=False)
    energy_efficient = models.BooleanField(default=False)
    image_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name