from rest_framework import viewsets, mixins

class ReadModelViewSet(mixins.RetrieveModelMixin,
					mixins.ListModelMixin,
					viewsets.GenericViewSet):
	
	pass