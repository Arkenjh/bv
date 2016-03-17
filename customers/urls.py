# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomersViewSet, base_name='api_customers')
urlpatterns = router.urls