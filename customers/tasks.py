from __future__ import absolute_import
from celery import shared_task
from celery.decorators import task

# crontab
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
	print("add task")
	return x + y

@shared_task
def mul(x, y):
	return x * y

@shared_task
def xsum(numbers):
	return sum(numbers)


@periodic_task(
	run_every=(crontab(minute='*/1')),
	name="task_save_latest_flickr_image",
	ignore_result=True
)
def task_save_latest_flickr_image():
	print("### crontab here ### ;)")
	logger.info("Saved image from Flickr")	