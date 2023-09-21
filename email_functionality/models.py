from django.db import models
from django.contrib.auth.models import User


class Mails(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.CharField(max_length=5000, null=True, blank=True)
    sender = models.EmailField()
    recipient = models.EmailField()
    status = models.CharField(max_length=20)
    date_time = models.DateTimeField(auto_now_add=True)
