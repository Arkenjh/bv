# -*- coding: utf-8 -*-
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profile', views.UserViewSet, base_name='api_user')
router.register(r'userstore', views.UserStoreViewSet, base_name='api_userstore')
router.register(r'test', views.TestViewSet, base_name='api_test')
urlpatterns = router.urls