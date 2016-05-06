# -*- coding: utf-8 -*-
from rest_framework import routers
from after_sales_service import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'ticket', views.TicketViewSet, base_name='ticket')
router.register(r'product', views.ProductViewSet, base_name='product')
router.register(r'problem', views.ProblemViewSet, base_name='problem')
router.register(r'warranty', views.WarrantyViewSet, base_name='warranty')
router.register(r'file', views.FileViewSet, base_name='file')
router.register(r'equipment-loan', views.EquipmentLoanViewSet, base_name='equipment-loan')
router.register(r'loan-history', views.LoanHistoryViewSet, base_name='loan-history')
router.register(r'customer-history', views.CustomerHistoryViewSet, base_name='customer-history')

urlpatterns = router.urls