from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime

from stores.models import Stores
from after_sales_service.models import Product, Ticket, Problem, Comment
from products.models import Products, PRODUCTS_CHOICES
from companies.models import Company, SUPPLIERS_CHOICES

class CommentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Comment	

class ProblemSerializer(serializers.ModelSerializer):
	
	content = serializers.CharField(allow_blank=True)

	class Meta:
		model = Problem	

class TicketSerializer(serializers.ModelSerializer):

	created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
	store = serializers.HiddenField(default='store')	

	class Meta:
		model = Ticket	
		#depth = 2
		read_only_fields = ('id', 'created_by', 'store')

	def validate_store(self, value):
		return self.context['request'].user.profile.store

class ProductSerializer(serializers.ModelSerializer):
	product = serializers.ChoiceField(PRODUCTS_CHOICES, write_only=True)
	supplier = serializers.ChoiceField(SUPPLIERS_CHOICES, write_only=True)
	#problem = ProblemSerializer()

	class Meta:
		model = Product	
		read_only_fields = ('id', 'created_by')

#	def validate_store(self, value):
#		print("### validate store ###")
#		return self.context['request'].user.profile.store

	def validate_product(self, value):
		return Products.objects.get(id=value)

	def validate_problem(self, value):
		print(value)
		problem, created = Problem.objects.get_or_create(content=value)

		return problem

	def validate_supplier(self, value):
		print(value)
		return Company.objects.get(id=value)

	def create(self, validated_data):
		print(validated_data)

		product = Product.objects.create(**validated_data)
		product.save()

		return product	