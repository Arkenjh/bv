from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime

from products.models import Products, Brand

class BrandSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Brand	

class ProductsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Products
		#depth = 2
		read_only_fields = ('id', 'created_by')