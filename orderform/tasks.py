from celery.decorators import task
from celery.utils.log import get_task_logger
from .emails import send_order_email
from .util import send_order_sms




logger = get_task_logger(__name__)

#@task(name="send_order_email_task")
#def send_order_email_task(first_name, email, purchase_item):
#    logger.info("Sent order email")
#    return send_order_email(first_name, email, purchase_item)

@app.task(name="send_order_sms_task")
def send_order_sms_task(phoneNumber):
    logger.info("Sent order sms")
    return send_order_sms(phoneNumber)

#@task(name="send_new_order_sms_task")
#def send_new_order_sms_task(first_name):
#    logger.info("Sent new order sms")
#    return send_order_sms(first_name)