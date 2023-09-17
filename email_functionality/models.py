from django.db import models
from django.contrib.auth.models import User


class Mails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)
    sender = models.EmailField()
    recipient = models.EmailField()
    status = models.CharField(max_length=20)
