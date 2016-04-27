from django.contrib import admin

from after_sales_service.models import Ticket, Product, Problem
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Product)
admin.site.register(Problem)