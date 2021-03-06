from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from . import settings
from celery.decorators import task
from celery.utils.log import get_task_logger


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ordersite.settings')

app = Celery('ordersite')

app.config_from_object('django.conf:settings')#, namespace='CELERY')

app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from orderform.util import send_order_sms

logger = get_task_logger(__name__)

@app.task(name="send_order_sms_task")
def send_order_sms_task(phoneNumber):
    logger.info("Sent order sms")
    return send_order_sms(phoneNumber)