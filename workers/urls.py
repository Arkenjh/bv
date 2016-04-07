# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'workplaces', views.WorkplacesViewSet, base_name='api_workplaces')
router.register(r'workers', views.WorkersViewSet, base_name='api_workers')
router.register(r'myworkers', views.MyWorkersViewSet, base_name='api_myworkers')
urlpatterns = router.urls