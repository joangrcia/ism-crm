from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class PersonalDetail(models.Model):

    ID_CHOICES = [
        ('idcard', 'ID Card'),
        ('passport', 'Passport'),
    ]

    MARITAL_CHOICES = [
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField(blank=True)
    id_type = models.CharField(max_length=20, choices=ID_CHOICES)
    id_number = models.BigIntegerField()
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class BankDetail(models.Model):
    user = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    bank_account = models.BigIntegerField()
    bank_address = models.CharField(max_length=100)
    swift_code = models.BigIntegerField(blank=True, default=0)
    bank_name = models.CharField(max_length=100)


class Wallet(models.Model):
    user = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE)
    wallet = models.BigIntegerField()
