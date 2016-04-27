# -*- coding: utf-8 -*-
from rest_framework import routers
from after_sales_service import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'ticket', views.TicketViewSet, base_name='ticket')
router.register(r'product', views.ProductViewSet, base_name='product')
router.register(r'problem', views.ProblemViewSet, base_name='problem')

urlpatterns = router.urls