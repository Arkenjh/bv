from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime

from locales.models import FrenchDepartments

class FrenchDepartmentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = FrenchDepartments
		fields = ('name',)

		