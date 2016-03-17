from django.contrib import admin

# Register your models here.
from stores.models import Stores, GroupStores, UserStore

admin.site.register(Stores)
admin.site.register(GroupStores)
admin.site.register(UserStore)