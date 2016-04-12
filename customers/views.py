from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from customers.serializers import CustomersSerializer
from customers.models import Customers


class CustomersViewSet(viewsets.ModelViewSet):
	serializer_class = CustomersSerializer

	def get_queryset(self):
		return Customers.objects.by_store(user=self.request.user)
	