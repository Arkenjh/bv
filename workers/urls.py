# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'workplaces', views.WorkplacesViewSet, base_name='api_workplaces')
router.register(r'workers', views.WorkersViewSet, base_name='api_workers')
urlpatterns = router.urls