from django.contrib import admin
from .models import User, Product, UserRating


# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(UserRating)