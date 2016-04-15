# -*- coding: utf-8 -*-
from rest_framework import routers
from reports import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'reports', views.ReportsViewSet, base_name='reports')
router.register(r'test', views.TestView, base_name='reports')
router.register(r'snippets', views.Fuck.as_view(), base_name='snippets')

urlpatterns = router.urls