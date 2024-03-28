from django.db import models
from django.contrib.auth.models import User
from apps.trading_account_app.models import TradingAccount
from django.core.exceptions import ValidationError
from django.utils import timezone

class MibAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return str(self.user)
    

class IbAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    account_number = models.OneToOneField(TradingAccount,on_delete=models.CASCADE)
    is_confirm = models.BooleanField(default=False)
    is_ib = models.BooleanField(default=False)
    is_sub_ib = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if IbList.objects.filter(client_account=self.user).exists():
            self.is_ib = False
            self.is_sub_ib = True
        else:
            self.is_ib = True
            self.is_sub_ib = False

        super().save(*args, **kwargs)

class MibList(models.Model):
    mib = models.ForeignKey(MibAccount, on_delete=models.CASCADE)
    ib_account = models.OneToOneField(IbAccount, on_delete=models.CASCADE)

    # def clean(self):
    #     if IbAccount.objects.filter(user=self.client_account).exists():
    #         raise ValidationError('Client account is already an IB.')

    #     existing_ib_lists = IbList.objects.filter(client_account=self.client_account)
    #     if existing_ib_lists.exists():
    #         raise ValidationError('Client account already exists for another IB.')

    #     super().clean()

    def __str__(self):
        return str(self.mib)

class IbList(models.Model):
    ib = models.ForeignKey(IbAccount, on_delete=models.CASCADE)
    client_account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ib_lists')

    def clean(self):
        if IbAccount.objects.filter(user=self.client_account).exists():
            raise ValidationError('Client account is already an IB.')

        existing_ib_lists = IbList.objects.filter(client_account=self.client_account)
        if existing_ib_lists.exists():
            raise ValidationError('Client account already exists for another IB.')

        super().clean()

    def __str__(self):
        return str(self.ib)
    
class History(models.Model):
    CHOICES1 = [
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]
    CHOICES2 = [
        ('IB', 'IB'),
        ('SUB IB', 'SUB IB'),
        ('MIB', 'MIB'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=CHOICES1)
    request = models.CharField(max_length=10, choices=CHOICES2)
    created_at = models.DateTimeField(default=timezone.now)
