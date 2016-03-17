from django.contrib.auth.models import User, Group
from rest_framework import serializers
from reports import models
from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class StoresSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Stores
		fields = ('name', 'workers',)

class SalesSerializer(serializers.HyperlinkedModelSerializer):
	#worker = serializers.StringRelatedField(many=False,)
	report = serializers.StringRelatedField(many=False)

	class Meta:
		model = models.Sales
		fields = ('report',)

class WorkersSerializer(serializers.ModelSerializer):
	sales = SalesSerializer(source='get_sales', many=True, read_only=True)

	class Meta:
		model = models.Workers
		fields = ('name', 'sales')

class WorkerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Workers
		fields = ('name',)

class CommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Comments
		fields = ('content',)

class ReportsSerializer(serializers.ModelSerializer):
	#store = StoresSerializer(read_only=True)
	comment = CommentsSerializer(many=False, write_only=False)
	#workers = WorkerSerializer(source='get_workers', many=True, read_only=True)
	workers = WorkerSerializer(many=True, read_only=True)
	#created_by = SimpleUserSerializer(read_only=True)
	created_by = serializers.ReadOnlyField(source='created_by.username',)
	store = serializers.ReadOnlyField(source='store.name',)
	comments = serializers.ReadOnlyField(source='comment.content',)
	workers_list = serializers.MultipleChoiceField(models.WORKERS_CHOICES, write_only=True)
	#api_url = serializers.SerializerMethodField('get_api_url', read_only=True)

	class Meta:
		model = models.Reports
		#fields = ('store', 'date', 'qty_inkjet_1', 'qty_inkjet_2', 'inkjet_ratio', 
		#	'qty_laser_1', 'qty_laser_2', 'laser_ratio', 'comment', 'workers', 'created_by',)		
		#depth = 2
		read_only_fields = ('id', 'created_by', 'api_url')


	def get_api_url(self, obj):
		return "#/%s" % obj.id

	def create(self, validated_data):
		print(validated_data)
		data = {}
		#profile_data = validated_data.pop('date')
		# rest_framework.request.Request

		u = User.objects.get(id=self.context['request'].user.id)
		s = models.Stores.objects.get(id=u.userstore.store.id)
		m = models.Comments.objects.create(content=str(validated_data['comment']['content']))

		data['store'] = s
		data['created_by'] = u
		data['comment'] = m
		data['qty_laser_2'] = validated_data['qty_laser_2']
		data['qty_laser_1'] = validated_data['qty_laser_1']
		#data['date'] = str(datetime.strptime(validated_data['date'], '%Y-%m-%d').date())
		data['date'] = validated_data['date'].strftime('%Y-%m-%d')
		data['qty_inkjet_2'] = validated_data['qty_inkjet_2']
		data['qty_inkjet_1'] = validated_data['qty_inkjet_1']

		r = models.Reports.objects.create(**data)
		r.save()

		for worker_id in validated_data['workers_list']:
			w = models.Workers.objects.get(id=worker_id)
			r.workers.add(w)

		r.save()
		return r		