from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from reports import models
from datetime import datetime
from stores.serializers import StoresSerializer
from stores.models import Stores, STORES_CHOICES
from customers.models import Customers
from api import utils


class CustomersSerializer(serializers.ModelSerializer):

	#store = StoresSerializer(read_only=True, required=False)
	created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
	store = serializers.HiddenField(default='store')
	#store = serializers.ReadOnlyField(required=False)
	#full_name = serializers.CharField()
	#stores = serializers.ChoiceField(STORES_CHOICES, write_only=True)

	class Meta:
		model = Customers
		read_only_fields = ('id', 'created_by', 'added', 'updated', 'store', 'fullname')
		#fields = ('firstname','lastname','store')

#		validators = [
#			UniqueTogetherValidator(
#				queryset=Customers.objects.all(),
#				fields=('firstname', 'lastname')
#			)
#		]

	def validate_store(self, value):
		print("### validate store ###")
		return self.context['request'].user.profile.store

	def validate(self, attrs):
		print("### validate here ###")
		print(attrs)
		#profile = self.context['request'].user.profile

		#results = utils.getProfile(self.context)
		#attrs['store'] = profile.store
		#attrs['created_by'] = profile.user		
		#raise serializers.ValidationError("error")
		return attrs

	def create(self, validated_data):
		print(validated_data)

		#profile = self.context['request'].user.profile

		#results = utils.getProfile(self.context)
		#validated_data['store'] = profile.store
		#validated_data['created_by'] = profile.user


		r = Customers.objects.create(**validated_data)
		r.save()
		return r