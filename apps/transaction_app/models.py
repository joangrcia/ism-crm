from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from apps.trading_account_app.models import TradingAccount

# Create your models here.
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, default=5)
    bank_method = models.CharField(max_length=10)
    is_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return str(self.user)
    
class DepositHistory(models.Model):

    CHOICES = [
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, default=5)
    bank_method = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return str(self.user)
    
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, default=5)
    bank_method = models.CharField(max_length=10)
    is_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return str(self.user)
    
class WithdrawHistory(models.Model):

    CHOICES = [
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, default=5)
    bank_method = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return str(self.user)
    
class IntTrans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    from_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, related_name='transfers_from_inttrans', default=1)
    to_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, related_name='transfers_to_inttrans', default=1)
    is_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"Transfer from {self.from_account} to {self.to_account} by {self.user}"

class IntTransHistory(models.Model):
    CHOICES = [
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    from_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, related_name='transfers_from_history', default=1)
    to_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, related_name='transfers_to_history', default=1)
    status = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return str(self.user)
