from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime

from stores.models import Stores
from after_sales_service.models import Product, Ticket, Problem, Comment, Warranty, Files, EquipmentLoan, LoanHistory, CustomerHistory, SharedData
from products.models import Products, PRODUCTS_CHOICES
from companies.models import Company, SUPPLIERS_CHOICES
from customers.models import Customers
from customers.serializers import CustomersSerializer
from bv.validators import FileValidator

class FileSerializer(serializers.ModelSerializer):
	store = serializers.HiddenField(default='store')
	available = serializers.HiddenField(default=True)
	#size = serializers.HiddenField()
	#content_type = serializers.HiddenField()
	content = serializers.FileField(validators=[FileValidator(max_size=24*1024*1024,allowed_extensions=('pdf','jpg','jpeg','png',))])

	class Meta:
		model = Files
		read_only_fields = ('id', 'created_by','size','name','content_type')

	def validate_store(self, value):
		return self.context['request'].user.profile.store

	def validate(self, data):
		###  HACK  ### ajout du content type à la validation du post, pas terrible
		request = self.context.get("request")
		if request and hasattr(request, "FILES"):
			f = request.FILES.getlist('content')[0]
			data['content_type'] = f.content_type
			data['name'] = f.name
			data['size'] = f.size

		return data

class EquipmentLoanSerializer(serializers.ModelSerializer):
	store = serializers.HiddenField(default='store')


	def validate_store(self, value):
		return self.context['request'].user.profile.store

	class Meta:
		model = EquipmentLoan
		read_only_fields = ('id', 'store',)


class FilteredListSerializer(serializers.ListSerializer):

	def to_representation(self, data):
		data = data.filter(store=self.request.user.profile.store.id, edition__hide=False)
		print(data)
		return super(FilteredListSerializer, self).to_representation(data)


class LoanHistorySerializer(serializers.ModelSerializer):
	store = serializers.HiddenField(default='store')
	created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
	equipment = EquipmentLoanSerializer(read_only=True)

	def get_fields(self, *args, **kwargs):
		fields = super(LoanHistorySerializer, self).get_fields(*args, **kwargs)
		view = self.context['view']
		user = view.request.user
		store = user.profile.store
		#fields['equipment'].queryset = EquipmentLoan.objects.filter(store=store.id, available=True)
		#fields['customer'].queryset = Customers.objects.filter(store=store.id)
		fields['equipments'] = serializers.ChoiceField(EquipmentLoan.objects.choices(user=user), write_only=True)
		fields['customers'] = serializers.ChoiceField(Customers.objects.choices(user=user), write_only=True)

		return fields

	def validate_store(self, value):
		return self.context['request'].user.profile.store

	def validate(self, data):
		
		data['equipment'] = EquipmentLoan.objects.get(id=data['equipments'])
		data['customer'] = Customers.objects.get(id=data['customers'])
		data.pop('equipments')
		data.pop('customers')

		return data

	class Meta:
		model = LoanHistory
		read_only_fields = ('id','created_by','store','equipment','customer',)
		depth = 1

class WarrantySerializer(serializers.ModelSerializer):

	class Meta:
		model = Warranty

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

class SharedDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = SharedData
		fields = ('id', 'content')

class CustomerHistorySerializer(serializers.ModelSerializer):
	
	store = serializers.HiddenField(default='store')
	ticket = serializers.HiddenField(default='ticket')
	event = SharedDataSerializer(read_only=True)
	created_by = serializers.HiddenField(default='created_by')
	comment = CommentSerializer(read_only=True)

	class Meta:
		model = CustomerHistory
		read_only_fields = ('id', 'ticket', 'store')