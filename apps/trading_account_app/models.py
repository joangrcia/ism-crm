from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(default=0)
    acoount_deposit = models.BigIntegerField(default=0)
    client_group = models.CharField(max_length=100, blank=True)