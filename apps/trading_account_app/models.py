from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
    
class TradingProduct(models.Model):
    group = models.CharField(default="")
    leverage = models.BigIntegerField(default=0)
    min_deposit = models.BigIntegerField(default=0)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.group)
    
class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(default=0)
    account_deposit = models.BigIntegerField(default=0)
    client_group = models.OneToOneField(TradingProduct, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.account_number)