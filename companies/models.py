# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from stores.models import Stores
from datetime import timedelta

from companies.validators import FileValidator

class Brands(models.Model):
	name = models.CharField("nom", max_length=50, blank=False)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

class Tags(models.Model):
	name = models.CharField("nom", max_length=50, blank=False)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

TAGS_CHOICES = [(tag.id, tag.name) for tag in Tags.objects.filter(available=True)]

class Sectors(models.Model):
	county = models.CharField("departement / région", max_length=50, blank=False)

class Country(models.Model):
	name = models.CharField("pays", max_length=30)
	short = models.CharField("nom court", max_length=30, blank=False)

	def __str__(self):
		return self.name

class Roles(models.Model):
	name = models.CharField("nom", max_length=50)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

class Labels(models.Model):
	name = models.CharField("nom", max_length=50)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

class Company(models.Model):
	name = models.CharField("nom", max_length=50)
	short = models.CharField("nom court", max_length=30)
	url = models.CharField("url", max_length=100, default="", blank=True)
	phone = models.CharField("téléphone", max_length=20, default="", blank=True)
	fax = models.CharField("fax", max_length=20, default="" ,blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	role = models.ForeignKey(Roles, verbose_name="type")
	available = models.BooleanField("actif", null=False, default=True)
	tags = models.ManyToManyField(Tags, blank=False, verbose_name="tag(s)")

	def __str__(self):
		return self.name

class Persons(models.Model):
	name = models.CharField("nom", max_length=50)
	email = models.EmailField("email", default="", blank=True)
	phone_1 = models.CharField("téléphone #1", max_length=20, default="", blank=True)
	phone_2 = models.CharField("téléphone #2", max_length=20, default="", blank=True)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.name

class Address(models.Model):
	label = models.ForeignKey(Labels, verbose_name="étiquette")
	address_1 = models.CharField("adresse", max_length=100, default="")
	address_2 = models.CharField("adresse (complement)", max_length=100, default="", blank=True)
	zipcode = models.CharField("code postal", max_length=10, default="")
	town = models.CharField("ville", max_length=50, default="")
	country = models.ForeignKey(Country, verbose_name="pays")
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	company = models.ForeignKey(Company, verbose_name="compagnie")
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.label.name

class Files(models.Model):
	company = models.ForeignKey(Company, verbose_name="compagnie")
	title = models.CharField("nom", max_length=50, default="")
	name = models.CharField("fichier", max_length=50, default="")
	size = models.IntegerField("taille", default=0)
	content = models.FileField(upload_to='uploads/company/')
	#content = models.FileField(upload_to='uploads/company/',validators=FileValidator(max_size=24*1024*1024,allowed_extensions=('pdf',)))
	content_type = models.CharField("type", max_length=50, default="")
	label = models.ForeignKey(Labels, verbose_name="étiquette") 
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	available = models.BooleanField("actif", null=False, default=True)
	#content = RestrictedFileField(upload_to='uploads/company/', content_types=['application/msword', 'application/pdf', 'application/vnd.oasis.opendocument.text'],max_upload_size=5242880)
	def __str__(self):
		return self.title


#def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	#return 'user_{0}/{1}'.format(instance.user.id, filename)

class Contacts(models.Model):
	company = models.ForeignKey(Company, verbose_name="compagnie")
	person = models.ForeignKey(Persons, verbose_name="contact") 
	label = models.ForeignKey(Labels, verbose_name="étiquette")
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.person.name

class Process(models.Model):
	title = models.CharField("nom", max_length=50)
	brand = models.ForeignKey(Brands, verbose_name="marque", null=True)
	content = models.TextField("procédure", default="")
	delay = models.DurationField("délai", default=timedelta())
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	company = models.ForeignKey(Company, verbose_name="compagnie")
	address = models.ForeignKey(Address, verbose_name="adresse", null=True)
	files = models.ManyToManyField(Files, verbose_name="tag(s)", null=True, blank=True)
	contact = models.ForeignKey(Contacts, verbose_name="contact", null=True)
	url = models.URLField("url", null=True, blank=True)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return self.title

class Departments(models.Model):
	name = models.CharField("nom", max_length=50)
	phone = models.CharField("téléphone", max_length=20,default="",blank=True)
	fax = models.CharField("fax", max_length=20,default="",blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	label = models.ForeignKey(Labels, verbose_name="étiquette")
	available = models.BooleanField("actif", null=False, default=True)
	#contacts = models.ManyToManyField(Tags, null=True, verbose_name="tag(s)")
	address = models.ForeignKey(Tags, null=True, verbose_name="tag(s)")
	company = models.ForeignKey(Company, verbose_name="compagnie")

	def __str__(self):
		return self.name	