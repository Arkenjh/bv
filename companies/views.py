from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from companies import serializers as se
from companies import models as mo

from locales.models import Countries

from tagging.models import Tag

class TagsViewSet(viewsets.ModelViewSet):
	serializer_class = se.TagsSerializer

	def get_queryset(self):
		return mo.Tags.objects.all()

class BrandsViewSet(viewsets.ModelViewSet):
	serializer_class = se.BrandsSerializer

	def get_queryset(self):
		return mo.Brands.objects.all()

class RolesViewSet(viewsets.ModelViewSet):
	serializer_class = se.RolesSerializer

	def get_queryset(self):
		return mo.Roles.objects.all()

class LabelsViewSet(viewsets.ModelViewSet):
	serializer_class = se.LabelsSerializer

	def get_queryset(self):
		return mo.Labels.objects.filter(available=True)

class CountryViewSet(viewsets.ModelViewSet):
	serializer_class = se.CountrySerializer

	def get_queryset(self):
		return Countries.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
	serializer_class = se.CompanySerializer

	def get_queryset(self):
		return mo.Company.objects.all()

class ContactsViewSet(viewsets.ModelViewSet):
	serializer_class = se.ContactsSerializer

	def get_queryset(self):
		return mo.Contacts.objects.filter(available=True)

class ProcessViewSet(viewsets.ModelViewSet):
	serializer_class = se.ProcessSerializer

	def get_queryset(self):
		return mo.Process.objects.filter(available=True)		

class FilesViewSet(viewsets.ModelViewSet):
	serializer_class = se.FilesSerializer

	def get_queryset(self):
		return mo.Files.objects.all()

	def pre_save(self, obj):
		print(self.request.FILES)
		#obj.content_type = self.request.FILES

class AddressViewSet(viewsets.ModelViewSet):
	serializer_class = se.AddressSerializer

	def get_queryset(self):
		return mo.Address.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
	serializer_class = se.DepartmentSerializer

	def get_queryset(self):
		return mo.Departments.objects.all()		

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = se.TagSerializer		