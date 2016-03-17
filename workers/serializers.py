from django.contrib.auth.models import User, Group
from rest_framework import serializers
from workers import models
from datetime import datetime

class WorkplacesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Workplaces
		fields = ('name', 'short')

class WorkerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Workers
		fields = ('name',)

class WorkersSerializer(serializers.ModelSerializer):
	#workplace = WorkplacesSerializer(many=False, write_only=False)
	work = serializers.ReadOnlyField(source='workplace.name',)
	workplace = serializers.ChoiceField(models.WORKPLACES_CHOICES, write_only=True)

	class Meta:
		model = models.Workers
		fields = ('name', 'workplace', 'work')

	def create(self, validated_data):
		print(validated_data)

		#u = User.objects.get(id=self.context['request'].user.id)
		#workplace = models.Workplaces.objects.get(id=validated_data['workplace'])
		validated_data['workplace'] = models.Workplaces.objects.get(id=validated_data['workplace'])

		w = models.Workers.objects.create(**validated_data)
		w.save()

		return w


	def update(self, instance, validated_data):
		print(validated_data)

		validated_data['workplace'] = models.Workplaces.objects.get(id=validated_data['workplace'])
		#instance.update(**validated_data)

		instance.name = validated_data.get('name', instance.name)
		instance.workplace = validated_data.get('workplace', instance.workplace)

		instance.save()

		return instance		