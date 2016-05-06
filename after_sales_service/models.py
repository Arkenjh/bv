from django.db import models
from django.conf import settings
from products.models import Products, SubCategory, Brand
from companies.models import Company
from customers.models import Customers
from stores.models import Stores

from datetime import timedelta
from django.db import transaction
from tagging.fields import TagField



class EquipmentLoanManager(models.Manager):

	def choices(self, user):
		return [(equipment.id, equipment.description) for equipment in EquipmentLoan.objects.filter(store=user.profile.store.id, available=True)]		

	def from_store(self, user):
		return super(EquipmentLoanManager, self).get_queryset().filter(store=user.profile.store.id)

class EquipmentLoan(models.Model):
	store = models.ForeignKey(Stores, verbose_name="magasin", null=False, blank=False)
	description = models.CharField("description", max_length=200, blank=False, null=False)
	available = models.BooleanField("actif", null=False, blank=False, default=True)

	def __str__(self):
		return "%s" % (self.description)

	objects = EquipmentLoanManager()

class LoanHistoryManager(models.Manager):

	def from_store(self, user):
		return super(LoanHistoryManager, self).get_queryset().filter(store=user.profile.store.id)

class LoanHistory(models.Model):
	store = models.ForeignKey(Stores, verbose_name="magasin", null=False, blank=False)
	equipment = models.ForeignKey(EquipmentLoan, verbose_name="matériel", null=False, blank=False)
	customer = models.ForeignKey(Customers, null=True, blank=True, verbose_name="client")
	start = models.DateField("prêté le", blank=False, null=False)
	end = models.DateField("rendu le", null=True, blank=True)
	closed = models.BooleanField("terminé", null=False, blank=False, default=False)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="utilisateur")

	objects = LoanHistoryManager()

class Settings(models.Model):
	store = models.OneToOneField(Stores, verbose_name="magasin", null=False, blank=False)
	prefix = models.CharField("préfixe", max_length=3, blank=False, null=False)
	start = models.IntegerField("premier numéro", default=1000)
	current = models.IntegerField("numéro en cours", default=1000)

	class Meta:
		verbose_name_plural = "settings"	

	def __str__(self):
		return "%s - %s%d" % (self.store.name, self.prefix, self.current)

class Warranty(models.Model):
	description = models.CharField("description", max_length=200, blank=False, null=False)
	period = models.IntegerField("durée de garantie", default=24)
	store = models.BooleanField("garantie magasin", default=True)

	def __str__(self):
		return "%s (%d mois)" % (self.description, self.period)

	class Meta:
		verbose_name_plural = "warranties"		

class Problem(models.Model):
	content = models.TextField("problème", default="")
	tags = TagField()

	def __str__(self):
		return self.content

class Product(models.Model):
	product = models.ForeignKey(Products, verbose_name="produit")
	problem = models.ForeignKey(Problem, verbose_name="problème")
	supplier = models.ForeignKey(Company, verbose_name="fournisseur")
	warranty = models.ForeignKey(Warranty, verbose_name="garantie", blank=True, null=True)

	description = models.CharField("description du problème", max_length=200, blank=True)
	serial_number = models.CharField("numéro de série", max_length=50, blank=True)
	supplier_code = models.CharField("code produit", max_length=50, blank=True)

	purchase_date = models.DateField("date d'achat", blank=True, null=True)
	purchase_number = models.CharField("numéro de facture", max_length=20, blank=True)
	
	brand = models.ForeignKey(Brand, verbose_name="marque", blank=True)
	category = models.ForeignKey(SubCategory, verbose_name="catégorie", blank=True)


	def __str__(self):
		return self.product.name

class Comment(models.Model):
	content = models.TextField("problème", default="")

	def __str__(self):
		return self.content

class TicketManager(models.Manager):

	def by_store(self, user):
		return super(TicketManager, self).get_queryset().filter(store=user.profile.store.id)
"""
	def create(self, **kwargs):
		with transaction.atomic():

			store = kwargs.get('store', None)
			store_settings = Settings.objects.get(store=store.id)

			kwargs['reference'] = store_settings.current + 1

			print(store_settings)

			
			ticket = self.model(**kwargs)
			ticket.save(force_insert=True)
			
		return ticket
"""

class Ticket(models.Model):
	reference = models.IntegerField("référence", default="")
	products = models.ManyToManyField(Product, verbose_name="produit(s)", blank=True)
	store = models.ForeignKey(Stores, verbose_name="magasin", null=False, blank=False)
	customer = models.ForeignKey(Customers, null=True, blank=True, verbose_name="client")
	comment = models.ForeignKey(Comment, null=True, blank=True, verbose_name="commentaire")
	completed = models.BooleanField("terminé", default=False)
	created = models.DateTimeField("ajouté le", auto_now_add=True)
	updated = models.DateTimeField("modifié le", auto_now=True)
	last_activity = models.DateTimeField("dernière activité")
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="utilisateur")
	#files = models.ForeignKey(Files, verbose_name="fichier(s)")

	objects = TicketManager()

	def __str__(self):
		return "%s | ticket #%s" % (self.store.name, self.reference)

	def save(self, *args, **kwargs):
		if self.reference == "":
			store_settings = Settings.objects.get(store=self.store.id)
			store_settings.current += 1
			self.reference = store_settings.current
			store_settings.save()

		super(Ticket, self).save(*args, **kwargs)

class FilesManager(models.Manager):

	def from_ticket(self, ticket):
		return super(FilesManager, self).get_queryset().filter(ticket=ticket)

	def from_store(self, user):
		return super(FilesManager, self).get_queryset().filter(store=user.profile.store.id)

class Files(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")
	store = models.ForeignKey(Stores, verbose_name="magasin", null=False, blank=False)
	title = models.CharField("nom", max_length=50, default="")
	name = models.CharField("fichier", max_length=50, default="")
	size = models.IntegerField("taille", default=0)
	content = models.FileField(upload_to='uploads/ticket/')
	content_type = models.CharField("type", max_length=50, default="")
	created_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	available = models.BooleanField("actif", null=False, default=True)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "file"
		verbose_name_plural = "files"

	objects = FilesManager()

class SharedData(models.Model):
	CUSTOMER = 'CU'
	SUPPLIER = 'SU'
	STORE = 'ST'
	CHOICES = (
		(CUSTOMER, 'Client'),
		(SUPPLIER, 'Fournisseur'),
		(STORE, 'Magasin'),
	)
	category = models.CharField(max_length=2,
		choices=CHOICES,
		default=CUSTOMER)

	content = models.TextField("description", default="")
	short = models.CharField("code", max_length=3, blank=True, null=True)
	available = models.BooleanField("actif", null=False, default=True)

	def __str__(self):
		return "%s (%s)" % (self.content, self.category)

class SupplierHistory(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")

class CustomerHistory(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")
	store = models.ForeignKey(Stores, verbose_name="magasin", null=True, blank=True)
	event = models.ForeignKey(SharedData, verbose_name="evennement", null=True, blank=True)
	created = models.DateTimeField("ajouté le", auto_now_add=True)
	updated = models.DateTimeField("modifié le", auto_now=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="utilisateur")
	comment = models.ForeignKey(Comment, null=True, blank=True, verbose_name="commentaire")	

class StoreHistory(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")
