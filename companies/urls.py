# -*- coding: utf-8 -*-
from rest_framework import routers
from companies import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', views.TagsViewSet, base_name='api_tags')
router.register(r'brands', views.BrandsViewSet, base_name='api_brands')
router.register(r'roles', views.RolesViewSet, base_name='api_roles')
router.register(r'labels', views.LabelsViewSet, base_name='api_labels')
router.register(r'country', views.CountryViewSet, base_name='api_country')
router.register(r'company', views.CompanyViewSet, base_name='api_company')
router.register(r'contacts', views.ContactsViewSet, base_name='api_contacts')
router.register(r'process', views.ProcessViewSet, base_name='api_process')
router.register(r'files', views.FilesViewSet, base_name='api_files')
router.register(r'address', views.AddressViewSet, base_name='api_address')
urlpatterns = router.urls