from django.shortcuts import render
from rest_framework import viewsets
from products.serializers import BrandSerializer, ProductsSerializer
from products.models import Brand, Products

from rest_framework import filters

class BrandViewSet(viewsets.ModelViewSet):

	serializer_class = BrandSerializer

	def get_queryset(self):
		return Brand.objects.all()

class ProductsViewSet(viewsets.ModelViewSet):

	serializer_class = ProductsSerializer
	search_fields = ('name')
	filter_backends = (filters.DjangoFilterBackend,)

	def get_queryset(self):
		products = Products.objects.filter(brand=None)
		name = self.request.query_params.get('name', None)
		if name is not None:
			products = products.filter(name__contains=name)
		return products		