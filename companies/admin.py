from django.contrib import admin

from companies import models as mo


admin.site.register(mo.Tags)
admin.site.register(mo.Files)
admin.site.register(mo.Process)
admin.site.register(mo.Company)