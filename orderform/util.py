from django.template import Context, context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, message
from django.conf import settings
import requests
from requests.models import Response
from .forms import *


def send_order_sms(phoneNumber):

	PARAMS = {
		"username": "sedziah1@gmail.com",
		"password": "P@ssword.telqs",
		"from": "TELQS" ,
		"to": phoneNumber, 
		"message": render_to_string('order_message.txt')
			}

	response = requests.post('https://frog.wigal.com.gh/ismsweb/sendmsg/', params=PARAMS)
	if response.status_code == 200:
		return response
			
	else:
		error={
			"error":"true",
			"status_code": response.status_code,
			"message": "Internal server error"
		}
		return error
