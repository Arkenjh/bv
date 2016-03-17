# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, base_name='api_user')
router.register(r'group', views.GroupViewSet, base_name='api_group')
router.register(r'stores', views.StoresViewSet, base_name='api_stores')
router.register(r'sales', views.SalesViewSet, base_name='api_sales')
router.register(r'worker', views.WorkerViewSet, base_name='api_worker')
router.register(r'workers', views.WorkersViewSet, base_name='api_workers')
router.register(r'comments', views.CommentsViewSet, base_name='api_comments')
router.register(r'reports', views.ReportsViewSet, base_name='api_reports')
urlpatterns = router.urls