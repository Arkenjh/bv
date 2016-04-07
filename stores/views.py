from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from stores.serializers import StoresSerializer, GroupStoresSerializer
from stores.models import Stores, GroupStores

class StoreViewSet(viewsets.ModelViewSet):
	serializer_class = StoresSerializer

	def get_queryset(self):
		return Stores.objects.by_user(user=self.request.user)	

class StoresViewSet(viewsets.ModelViewSet):
	queryset = Stores.objects.all()
	serializer_class = StoresSerializer

class GroupStoresViewSet(viewsets.ModelViewSet):
	queryset = GroupStores.objects.all()
	serializer_class = GroupStoresSerializer
