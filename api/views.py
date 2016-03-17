from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, StoresSerializer, SalesSerializer, WorkersSerializer, WorkerSerializer, CommentsSerializer, ReportsSerializer
from reports.models import Stores, Sales, Workers, Comments, Reports


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializer

class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer