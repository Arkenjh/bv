from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datetime import datetime
from django.contrib.auth import get_user_model
from django.conf import settings
from stores.serializers import StoresSerializer
from stores.models import UserStore


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = get_user_model()	
		fields = ('username', 'email')

class UserStoreSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserStore
		depth = 1

class TestSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	store = StoresSerializer(read_only=True)

	class Meta:
		model = UserStore