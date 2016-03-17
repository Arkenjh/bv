from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from workers.serializers import WorkerSerializer
from reports.models import Reports, Comments
from stores.models import Stores
from workers.models import Workers, WORKERS_CHOICES
from profiles.models import Profiles

class CommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = ('content',)

class ReportsSerializer(serializers.ModelSerializer):
	#comment = CommentsSerializer(required=False)
	comment = serializers.CharField(allow_blank=True)
	workers = WorkerSerializer(many=True, read_only=True)
	date = serializers.DateField()
	#created_by = serializers.ReadOnlyField(source='created_by.username',)
	#store = serializers.ReadOnlyField(source='store.name',)
	created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
	store = serializers.HiddenField(default='store')	
	#comments = serializers.ReadOnlyField(source='comment.content')
	workers_list = serializers.MultipleChoiceField(WORKERS_CHOICES, write_only=True)

	qty_inkjet_1 = serializers.IntegerField()
	qty_inkjet_2 = serializers.IntegerField()
	qty_laser_1 = serializers.IntegerField()
	qty_laser_2 = serializers.IntegerField()

	class Meta:
		model = Reports
		#fields = ('store', 'date', 'qty_inkjet_1', 'qty_inkjet_2', 'inkjet_ratio', 
		#	'qty_laser_1', 'qty_laser_2', 'laser_ratio', 'comment', 'workers', 'created_by',)		
		#depth = 2
		read_only_fields = ('id', 'created_by', 'api_url')


	def get_api_url(self, obj):
		return "#/%s" % obj.id

	def validate_store(self, value):
		print("### validate store ###")
		return self.context['request'].user.profile.store

	def validate_date(self, value):
		print("### validate date ###")
		if value > timezone.now().date():
			raise serializers.ValidationError("No future")
		return value

	def create(self, validated_data):
		print(validated_data)
		validated_data['date'] = validated_data['date'].strftime('%Y-%m-%d')
		workers_list = validated_data['workers_list']
		validated_data.pop('workers_list')
		
		report = Reports.objects.create(**validated_data)
		report.add_workers(workers_list)
		report.save()

		return report

	def update(self, instance, validated_data):

		instance.qty_inkjet_1 = validated_data.get('qty_inkjet_1', instance.qty_inkjet_1)
		instance.qty_inkjet_2 = validated_data.get('qty_inkjet_2', instance.qty_inkjet_2)
		instance.qty_laser_1 = validated_data.get('qty_laser_1', instance.qty_laser_1)
		instance.qty_laser_2 = validated_data.get('qty_laser_2', instance.qty_laser_2)
		#instance.comment.content = validated_data.get('comment', instance.comment.content)
		instance.set_comment(validated_data.get('comment'))

		instance.save()

		return instance		