from django.contrib import admin

from workers.models import Workers, Workplaces

admin.site.register(Workers)
admin.site.register(Workplaces)