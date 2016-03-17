from django.contrib.auth.models import User, Group
from stores.models import Stores, UserStore


def getProfile(context):
	u = User.objects.get(id=context['request'].user.id)
	us = UserStore.objects.get(user=u.id)
	s = Stores.objects.get(id=us.store.id)

	return dict(user=u, store=s)