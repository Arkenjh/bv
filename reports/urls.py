# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'reports', views.ReportsViewSet, base_name='api_reports')
#router.register(r'^snippets/$', views.index, base_name='api_index')
urlpatterns = router.urls