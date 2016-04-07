from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from workers.serializers import WorkplacesSerializer, WorkersSerializer
from workers.models import Workplaces, Workers

from stores.models import Stores


class WorkplacesViewSet(viewsets.ModelViewSet):
	queryset = Workplaces.objects.all()
	serializer_class = WorkplacesSerializer

class WorkersViewSet(viewsets.ModelViewSet):
	queryset = Workers.objects.all()
	serializer_class = WorkersSerializer

class MyWorkersViewSet(viewsets.ModelViewSet):
	serializer_class = WorkersSerializer

	def get_queryset(self):
		store = Stores.objects.by_user(user=self.request.user)
		#print(store[0].workers)

		return store[0].workers