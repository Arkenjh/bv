from django.contrib import admin

from after_sales_service.models import *


class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ("product",)

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Product, ProductAdmin)
admin.site.register(Problem)
admin.site.register(Warranty)	
admin.site.register(Files)
admin.site.register(Comment)
admin.site.register(Settings)