from django.http import response
from .models import NewOrders
from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import NewOrders
from .tasks import *
import requests


class OrderForm(ModelForm):

    def send_email(self):
        send_order_email_task.delay(
            self.cleaned_data['first_name'], self.cleaned_data['email'], self.cleaned_data['purchase_item'])
    
    def get_phone(self):
        return self.cleaned_data['primary_phone_number']

    def send_sms(self):
        send_order_sms_task.delay(
            self.cleaned_data['primary_phone_number'])

    
    class Meta:
        model = NewOrders
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}, ),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'primary_phone_number' : forms.TextInput(attrs={'class':'form-control'}),
            'alternate_phone_number' : forms.TextInput(attrs={'class':'form-control'}),
            'item_category' : forms.Select(attrs={'class':'form-control'}),
            'purchase_item' : forms.TextInput(attrs={'class':'form-control'}),
            'payment_mode' : forms.Select(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'comments' : forms.TextInput(attrs={'class':'form-control'}),
        }

