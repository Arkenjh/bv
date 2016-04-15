from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from django.contrib.auth.decorators import login_required
from reports.serializers import ReportsSerializer
from reports.models import Reports
from stores.models import Stores
from workers.models import Workers, WORKERS_CHOICES

from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import list_route
from bv import settings

class Fuck(APIView):

	def get(self, request):
		return Response(None)

#@login_required
class ReportsViewSet(viewsets.ModelViewSet):

	#queryset = Reports.objects.all()
	#queryset = Reports.objects.by_store(user=self.request.user)
	serializer_class = ReportsSerializer

	def get_queryset(self):
		return Reports.objects.by_store(user=self.request.user)

	def pre_save(self, obj):
		obj.created_by = self.request.user

	# For GET Requests
	@list_route()
	def get_email(self, request):

		from mailqueue.models import MailerMessage

		new_message = MailerMessage()
		new_message.subject = "oui c'est bien ce mail ..."
		new_message.to_address = "arkenjh@gmail.com"
		#new_message.bcc_address = "myblindcarboncopy@yo.com"
		new_message.from_address = "contact@ad-min.pro"
		new_message.content = "Mail content"
		new_message.html_content = "<h1>Mail Content</h1>"
		new_message.app = "Name of your App that is sending the email."
		new_message.save()

		return Response(new_message.html_content)

		#from django_mailer import send_mail
		# from django.core.mail import send_mail
		# subject = "fcuk mail"
		# message_body = "this is sparta !!!"
		# recipients = ['arkenjh@gmail.com']
		# res = send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, recipients)

		# return Response(res)


class TestView(viewsets.ViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'profile_list.html'

	def get(self, request):
		#queryset = Profile.objects.all()
		#return Response({'profiles': queryset})
		data = '<html><body><h1>Hello, world</h1></body></html>'
		return Response(data)


def index(request):
	from django_mailer import send_mail
	subject = "fcuk mail"
	message_body = "this is sparta !!!"
	recipients = ['arkenjh@gmail.com']

	send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, recipients)

	return render(request, 'index.html', dict())        