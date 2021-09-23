from django.contrib import admin
from .models import *


# Register your models here.
class NewOrdersAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'address', 
        'primary_phone_number', 
        'alternate_phone_number', 
        'item_category', 
        'purchase_item', 
        'payment_mode', 
        'email', 
        'comments'
        )

admin.site.register(NewOrders, NewOrdersAdmin)