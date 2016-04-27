from django.contrib import admin

from products.models import Products, Brand
# Register your models here.
admin.site.register(Products)
admin.site.register(Brand)