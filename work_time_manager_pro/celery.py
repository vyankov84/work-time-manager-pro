import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_time_manager_pro.settings')

app = Celery('work_time_manager_pro')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()