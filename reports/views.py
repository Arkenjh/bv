from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from django.contrib.auth.decorators import login_required
from reports.serializers import ReportsSerializer
from reports.models import Reports
from stores.models import Stores
from workers.models import Workers, WORKERS_CHOICES

from rest_framework.response import Response


#@login_required
class ReportsViewSet(viewsets.ModelViewSet):

	#queryset = Reports.objects.all()
	#queryset = Reports.objects.by_store(user=self.request.user)
	serializer_class = ReportsSerializer

	def get_queryset(self):
		return Reports.objects.by_store(user=self.request.user)

	def pre_save(self, obj):
		obj.created_by = self.request.user

def index(request):
	return render(request, 'index.html', dict())        