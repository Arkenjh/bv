from django.contrib import admin

from after_sales_service.models import *


class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ("product",)

class TicketAdmin(admin.ModelAdmin)	:
	exclude=("reference ",)
	readonly_fields=('reference',)	

# Register your models here.
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Problem)
admin.site.register(Warranty)	
admin.site.register(Files)
admin.site.register(Comment)
admin.site.register(Settings)
admin.site.register(EquipmentLoan)
admin.site.register(LoanHistory)
admin.site.register(SharedData)

admin.site.register(CustomerHistory)