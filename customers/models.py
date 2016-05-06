# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from stores.models import Stores

class CustomersManager(models.Manager):

	def choices(self, user):
		return [(customer.id, customer.full_name) for customer in Customers.objects.filter(store=user.profile.store.id)]		

	def by_store(self, user):
		return super(CustomersManager, self).get_queryset().filter(store=user.profile.store.id)

class Customers(models.Model):

	firstname = models.CharField("prénom", max_length=30,default="")
	lastname = models.CharField("nom de famille", max_length=30, blank=False)
	corporate_name = models.CharField("raison sociale", max_length=60,default="")
	professional = models.BooleanField("professionnel", null=False, default=False)

	email = models.EmailField("email", blank=True)
	phone_1 = models.CharField("téléphone #1", max_length=10,default="",blank=True)
	phone_2 = models.CharField("téléphone #2", max_length=10,default="",blank=True)
	address = models.CharField("adresse", max_length=60,default="",blank=True)
	zipcode = models.CharField("code postal", max_length=6,default="",blank=True)
	town = models.CharField("ville", max_length=20,default="",blank=True)
	country = models.CharField("pays", max_length=20,default="",blank=True)

	send_sms = models.BooleanField("envoie de sms", null=False, default=True)
	send_email = models.BooleanField("envoie de mail", null=False, default=True)

	store = models.ForeignKey(Stores, default=1, null=False, verbose_name="magasin")
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

	def _get_full_name(self):
		"Returns the person's full name."
		return self.corporate_name if self.corporate_name else '%s %s' % (self.firstname, self.lastname)

	full_name = property(_get_full_name)

	def __str__(self):
		return ("%s" % self.full_name)
		#return str(self.id)
		#return ("%s" % self.firstname).encode('ascii', errors='replace')

	def save(self,*args,**kwargs):
		if not self.pk:
			print("### override save method here ###")
		super(Customers,self).save(*args,**kwargs)

	objects = CustomersManager()

	#class Meta:
	#	unique_together = ('lastname', 'corporate_name', 'store')

#	def save(self, *args, **kwargs):
#		user = User.objects.get(settings.AUTH_USER_MODEL)
		#print(user.profile.store.name)
#		super(Customers, self).save(*args, **kwargs)

#	def save(self, *args, **kwargs):
#		if self.name == "Yoko Ono's blog":
#			return # Yoko shall never have her own blog!
#		else:
#			super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.

class Purchase(models.Model):
	customer = models.ForeignKey(Customers, null=False, blank=False, verbose_name="client")
