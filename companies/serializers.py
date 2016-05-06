from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime

from companies import models
from bv.validators import FileValidator

from locales.serializers import FrenchDepartmentsSerializer
from locales.models import FRENCH_DEPARTMENTS, Countries

class TagsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Tags
		fields = ('name',)

class BrandsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Brands
		fields = ('name',)

class RolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Roles
		fields = ('name',)

class LabelsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Labels
		fields = ('name',)

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Countries
		fields = ('name_fr_fr','alpha2',)

class CompanySerializer(serializers.ModelSerializer):

	#tags = serializers.MultipleChoiceField(models.TAGS_CHOICES, write_only=True)

	class Meta:
		model = models.Company
		read_only_fields = ('created_on','updated',)

class PersonsSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Persons
		read_only_fields = ('created_on','updated',)	

class ContactsSerializer(serializers.ModelSerializer):
	#sector = serializers.MultipleChoiceField(FRENCH_DEPARTMENTS, write_only=True)
	person = PersonsSerializer()

	class Meta:
		model = models.Contacts
		read_only_fields = ('created_on','updated',)

class ProcessSerializer(serializers.ModelSerializer):

	#contact = ContactsSerializer()

	class Meta:
		model = models.Process
		read_only_fields = ('created_on','updated',)	

class FilesSerializer(serializers.ModelSerializer):
	available = serializers.HiddenField(default=True)
	#size = serializers.HiddenField()
	#content_type = serializers.HiddenField()
	content = serializers.FileField(validators=[FileValidator(max_size=24*1024*1024,allowed_extensions=('pdf',))])

	class Meta:
		model = models.Files
		read_only_fields = ('created_on','updated','name','content_type','size')

	def validate(self, data):
		###  HACK  ### ajout du content type à la validation du post, pas terrible
		request = self.context.get("request")
		if request and hasattr(request, "FILES"):
			f = request.FILES.getlist('content')[0]
			data['content_type'] = f.content_type
			data['name'] = f.name
			data['size'] = f.size

		return data

class AddressSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Address
		read_only_fields = ('created_on','updated',)

class DepartmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Departments
		read_only_fields = ('created_on','updated',)

from tagging.models import Tag

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')		