from django.shortcuts import render
from django.urls import path
from .views import dashboard_view

app_name = 'email_functionality'

urlpatterns = [
    path('', dashboard_view, name='dashboard')
]
# Create your views here.
