from django.contrib.auth.models import User, Group
from rest_framework import serializers
from stores import models
from workers.models import WORKERS_CHOICES as WORKERS_CHOICES
from workers.serializers import WorkerSerializer
from datetime import datetime


class StoresSerializer(serializers.HyperlinkedModelSerializer):
	workers = serializers.MultipleChoiceField(WORKERS_CHOICES, write_only=True)
	#work = serializers.ReadOnlyField(source='workers.name',)
	work = WorkerSerializer(source='workers', many=True, read_only=True)

	class Meta:
		model = models.Stores
		fields = ('name', 'workers', 'work')

class GroupStoresSerializer(serializers.HyperlinkedModelSerializer):
	stores = serializers.MultipleChoiceField(models.STORES_CHOICES, write_only=True)

	class Meta:
		model = models.GroupStores
		fields = ('name', 'stores',)
	