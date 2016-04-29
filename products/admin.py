from django.contrib import admin

from products.models import *

# Register your models here.
admin.site.register(Products)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Division)