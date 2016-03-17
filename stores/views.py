from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from stores import serializers
from stores import models


class StoresViewSet(viewsets.ModelViewSet):
	queryset = models.Stores.objects.all()
	serializer_class = serializers.StoresSerializer

class GroupStoresViewSet(viewsets.ModelViewSet):
	queryset = models.GroupStores.objects.all()
	serializer_class = serializers.GroupStoresSerializer
