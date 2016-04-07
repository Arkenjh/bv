# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from workers.models import Workers

class StoresManager(models.Manager):

	def by_user(self, user):
		return super(StoresManager, self).get_queryset().filter(id=user.profile.store.id)

class GroupStores(models.Model):
	name = models.CharField("nom", max_length=30,unique=True)

	def __str__(self):
		return self.name	

class Stores(models.Model):
	name = models.CharField("nom", max_length=30,unique=True)
	fullname = models.CharField("nom complet", max_length=30)
	workers = models.ManyToManyField(Workers, verbose_name="employé(s)")
	group = models.ForeignKey(GroupStores,null=False, blank=False, verbose_name="groupe")
	

	def __str__(self):
		return self.name
		#return ("%s" % self.name).encode('ascii', errors='replace')

	objects = StoresManager()

class UserStore(models.Model):
	user = models.OneToOneField(User)
	store = models.ForeignKey(Stores,null=False, blank=False)

STORES_CHOICES = [(store.id, store.name) for store in Stores.objects.all()]