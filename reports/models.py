# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from workers.models import Workers
from stores.models import Stores
from django.db import transaction

class ReportsManager(models.Manager):

	def by_store(self, user):
		return super(ReportsManager, self).get_queryset().filter(store=user.profile.store.id)

	def create(self, **kwargs):
		with transaction.atomic():
			kwargs['comment'] = Comments.objects.create(content=kwargs.get('comment', ''))
			report = self.model(**kwargs)
			report.save(force_insert=True)
			
		return report		

class Comments(models.Model):
	content = models.TextField("commentaire", blank=False)

	def __str__(self):
		return self.content
		return ("%s" % self.content).encode('ascii', errors='replace')


class Reports(models.Model):

	store = models.ForeignKey(Stores, unique_for_date="date", blank=False, verbose_name="magasin")

	qty_inkjet_1 = models.IntegerField("Qte JE 1", default=0)
	qty_inkjet_2 = models.IntegerField("Qte JE 2", default=0)
	qty_laser_1 = models.IntegerField("Qte LA 1", default=0)
	qty_laser_2 = models.IntegerField("Qte LA 2", default=0)
	date = models.DateField("date", default=timezone.now, null=False)
	comment = models.ForeignKey(Comments, null=True, blank=True, verbose_name="commentaire")
	added = models.DateTimeField("ajouté le", auto_now_add=True)
	updated = models.DateTimeField("modifié le", auto_now=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="utilisateur")
	workers = models.ManyToManyField(Workers, blank=False, verbose_name="employé(s)")

	@property
	def inkjet_ratio(self):
		return float(self.qty_inkjet_2 * 100 / (self.qty_inkjet_1 + self.qty_inkjet_2))

	@property
	def laser_ratio(self):
		return float(self.qty_laser_2 * 100 / (self.qty_laser_1 + self.qty_laser_2))

	def get_inkjet_qty(self):
		return int(self.qty_inkjet_1 + self.qty_inkjet_2)

	def get_laser_qty(self):
		return int(self.qty_laser_1 + self.qty_laser_2)

	def get_total(self):
		return int(self.get_inkjet_qty + self.get_laser_qty)

	def add_comment(self, content):
		pass

	def set_comment(self, content):
		if content != self.comment.content:
			self.comment.content = content

	def add_worker(self, worker_id):
		w = Workers.objects.get(id=worker_id)
		self.workers.add(w)

	def add_workers(self, workers_list):
		for worker_id in workers_list:
			self.add_worker(worker_id)

	def save(self,*args,**kwargs):
		if not self.pk:
			print("### override save method here ###")
			#self.comment = Comments.objects.create(content=kwargs.get('comment', ''))
		super(Reports,self).save(*args,**kwargs)

	objects = ReportsManager()	

	class Meta:
		unique_together = ('store', 'date')

#WORKERS_CHOICES = [[elem, elem] for elem in Workers.objects.values_list('name', flat=True).order_by('name').distinct()]
#WORKERS_CHOICES = [(worker.id, worker.name) for worker in Workers.objects.all()]
#STORES_CHOICES = [[elem, elem] for elem in Stores.objects.values_list('name', flat=True).order_by('name').distinct()]