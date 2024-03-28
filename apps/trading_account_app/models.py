from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from apps.product_app.models import ProductTrading

class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    account_number = models.BigIntegerField(default=0, db_index=True)
    account_deposit = models.BigIntegerField(default=0)
    dm_group = models.ForeignKey(ProductTrading, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    last_updated = models.DateTimeField(auto_now=True, db_index=True)


    def __str__(self):
        return str(self.account_number)

