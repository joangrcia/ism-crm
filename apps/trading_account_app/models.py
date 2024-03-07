from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProductTrading(models.Model):
    name = models.CharField(max_length=20)
    leverage = models.IntegerField(default=0)
    min_deposit = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(default=0)
    account_deposit = models.BigIntegerField(default=0)
    dm_group = models.ForeignKey(ProductTrading, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.account_number)

