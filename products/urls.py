# -*- coding: utf-8 -*-
from rest_framework import routers
from products import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'brand', views.BrandViewSet, base_name='brand')
router.register(r'products', views.ProductsViewSet, base_name='products')

urlpatterns = router.urls