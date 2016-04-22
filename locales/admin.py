from django.contrib import admin

from locales import models


admin.site.register(models.FrenchDepartments)
admin.site.register(models.FrenchTowns)
admin.site.register(models.FrenchRegions)
admin.site.register(models.Countries)