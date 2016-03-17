from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from profiles import serializers
from stores.models import UserStore


class UserStoreViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.UserStoreSerializer
	queryset = UserStore.objects.all()

class TestViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.TestSerializer
	queryset = UserStore.objects.all()

class UserViewSet(viewsets.ModelViewSet):
	model = User
	serializer_class = serializers.UserSerializer

	def get_object(self):
		return self.request.user

	def list(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)	