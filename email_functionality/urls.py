from django.shortcuts import render
from django.urls import path
from .views import DashboardView

app_name = 'email_functionality'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard')
]
# Create your views here.
