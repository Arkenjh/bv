from django.shortcuts import render
from rest_framework import viewsets
from after_sales_service.serializers import *
from after_sales_service.models import *

from bv.customs_viewset import ReadModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

class CustomerHistoryViewSet(viewsets.ViewSet):

	def list(self, request):
		queryset = CustomerHistory.objects.filter()
		serializer = CustomerHistorySerializer(queryset, many=True)
		return Response(serializer.data)


	@detail_route(methods=['get'])
	def test(self, request, pk=None):
		queryset = CustomerHistory.objects.filter(id=pk)
		print(queryset)
		serializer = CustomerHistorySerializer(data=queryset)
		if serializer.is_valid():
		
			return Response(serializer.data)


class EquipmentLoanViewSet(viewsets.ModelViewSet):

	serializer_class = EquipmentLoanSerializer

	def get_queryset(self):
		#print(EquipmentLoan.objects.choices())
		return EquipmentLoan.objects.from_store(user=self.request.user).filter(available=True)

class LoanHistoryViewSet(viewsets.ModelViewSet):

	serializer_class = LoanHistorySerializer

	def get_queryset(self):
		return LoanHistory.objects.from_store(user=self.request.user)

	def get_serializer_context(self):
		context = super(LoanHistoryViewSet, self).get_serializer_context()
		return context

class FileViewSet(viewsets.ModelViewSet):

	serializer_class = FileSerializer

	def get_queryset(self):
		return Files.objects.from_store(user=self.request.user)

class TicketViewSet(viewsets.ModelViewSet):

	serializer_class = TicketSerializer

	def get_queryset(self):
		return Ticket.objects.by_store(user=self.request.user)

	def pre_save(self, obj):
		obj.created_by = self.request.user

	@detail_route(methods=['get'], url_path="customer")
	def get_customer_history(self, request, pk=None):
		queryset = CustomerHistory.objects.filter(ticket=pk)
		serializer = CustomerHistorySerializer(queryset, many=True)

		return Response(serializer.data)		

class ProductViewSet(viewsets.ModelViewSet):

	serializer_class = ProductSerializer

	def get_queryset(self):
		return Product.objects.all()

class ProblemViewSet(ReadModelViewSet):

	serializer_class = ProblemSerializer

	def get_queryset(self):
		return Problem.objects.all()

class WarrantyViewSet(ReadModelViewSet):

	serializer_class = WarrantySerializer

	def get_queryset(self):
		return Warranty.objects.all()		