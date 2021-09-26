from django import forms
from django.views.generic.edit import FormView
from requests.models import Response
from .models import NewOrders
from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, response
from .util import send_order_sms



class NewOrderView(FormView):
    form_class = OrderForm
    template_name = 'neworders.html'
 
    def form_valid(self, form):
        form.save()
        form.send_email()
        form.send_sms()
        msg = "Thanks for your order!"
        return HttpResponse(msg)