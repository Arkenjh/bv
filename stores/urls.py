# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'mystore', views.StoreViewSet, base_name='api_store')
router.register(r'stores', views.StoresViewSet, base_name='api_stores')
router.register(r'groups', views.GroupStoresViewSet, base_name='api_groups')
urlpatterns = router.urls