from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from workers import serializers
from workers import models


class WorkplacesViewSet(viewsets.ModelViewSet):
    queryset = models.Workplaces.objects.all()
    serializer_class = serializers.WorkplacesSerializer

class WorkersViewSet(viewsets.ModelViewSet):
    queryset = models.Workers.objects.all()
    serializer_class = serializers.WorkersSerializer