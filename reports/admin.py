from django.contrib import admin

# Register your models here.
from reports.models import Comments, Reports

admin.site.register(Comments)
admin.site.register(Reports)