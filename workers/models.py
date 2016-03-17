# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings


class Workplaces(models.Model):
	name = models.CharField("nom", max_length=100, unique=True, null=False)
	short = models.CharField("nom court", max_length=3, unique=True, null=False)

	def __str__(self):
		return self.name

class Workers(models.Model):
	name = models.CharField("Nom", max_length=30)
	workplace = models.ForeignKey(Workplaces, default=0, verbose_name="poste")

	def __str__(self):
		return self.name	

WORKPLACES_CHOICES = [(workplace.id, workplace.name) for workplace in Workplaces.objects.all()]
WORKERS_CHOICES = [(worker.id, worker.name) for worker in Workers.objects.all()]