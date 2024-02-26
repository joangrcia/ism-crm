from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(default=0)
    account_deposit = models.BigIntegerField(default=0)
    client_group = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
