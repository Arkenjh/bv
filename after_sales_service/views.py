from django.shortcuts import render
from rest_framework import viewsets
from after_sales_service.serializers import TicketSerializer, ProductSerializer, ProblemSerializer
from after_sales_service.models import Ticket, Product, Problem

class TicketViewSet(viewsets.ModelViewSet):

	serializer_class = TicketSerializer

	def get_queryset(self):
		return Ticket.objects.by_store(user=self.request.user)

	def pre_save(self, obj):
		obj.created_by = self.request.user

class ProductViewSet(viewsets.ModelViewSet):

	serializer_class = ProductSerializer

	def get_queryset(self):
		return Product.objects.all()

class ProblemViewSet(viewsets.ModelViewSet):

	serializer_class = ProblemSerializer

	def get_queryset(self):
		return Problem.objects.all()		