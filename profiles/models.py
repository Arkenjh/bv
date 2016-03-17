# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from stores.models import Stores

from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
	if created:
		profile = Profiles(user=instance)
		profile.save()

class Profiles(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", verbose_name="user")
	store = models.ForeignKey(Stores,null=False, blank=False, default=1)

	@property
	def username(self):
		return self.user.username

	@property
	def storename(self):
		return self.store.name

	@property
	def groupname(self):
		return self.store.group.name		

	class Meta:
		verbose_name = "Profile"
		verbose_name_plural = "Profiles"
		ordering = ("user",)

	def __str__(self):
		return "%s@%s [%s]" % (self.username, self.storename, self.groupname)