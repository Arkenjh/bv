from django.db import models
from django.conf import settings
from products.models import Products
from companies.models import Company
from customers.models import Customers
from stores.models import Stores

class Problem(models.Model):
	content = models.TextField("problème", default="")

	def __str__(self):
		return self.content

class Product(models.Model):
	product = models.ForeignKey(Products, verbose_name="produit")
	problem = models.ForeignKey(Problem, verbose_name="problème")
	supplier = models.ForeignKey(Company, verbose_name="fournisseur")

	serial_number = models.CharField("numéro de série", max_length=50, blank=True)
	supplier_code = models.CharField("code produit", max_length=50, blank=True)

	def __str__(self):
		return self.product.name

class Comment(models.Model):
	content = models.TextField("problème", default="")

class TicketManager(models.Manager):

	def by_store(self, user):
		return super(TicketManager, self).get_queryset().filter(store=user.profile.store.id)

class Ticket(models.Model):
	products = models.ManyToManyField(Product, verbose_name="produit(s)", blank=True)
	store = models.ForeignKey(Stores, verbose_name="magasin")
	customer = models.ForeignKey(Customers, null=True, blank=True, verbose_name="client")
	comment = models.ForeignKey(Comment, null=True, blank=True, verbose_name="commentaire")
	completed = models.BooleanField("terminé", default=False)
	created = models.DateTimeField("ajouté le", auto_now_add=True)
	updated = models.DateTimeField("modifié le", auto_now=True)
	last_activity = models.DateTimeField("dernière activité")
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="utilisateur")

	objects = TicketManager()

class SupplierHistory(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")

class CustomerHistory(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")

class StoreHistory(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name="ticket")
