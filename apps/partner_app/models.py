from django.db import models
from django.contrib.auth.models import User
from apps.trading_account_app.models import TradingAccount
# from django.db.models import OuterRef

class IbAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.OneToOneField(TradingAccount,on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class IbList(models.Model):
    ib = models.OneToOneField(IbAccount, on_delete=models.CASCADE)
    client_account = models.OneToOneField(User, on_delete=models.CASCADE)
