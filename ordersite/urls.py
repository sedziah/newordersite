from django.contrib import admin
from django.urls import path
from django.views.generic.base import View
from orderform.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('neworder/', NewOrderView.as_view(), name="neworder"),
]
