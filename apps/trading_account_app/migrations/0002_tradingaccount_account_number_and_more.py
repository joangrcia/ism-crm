# Generated by Django 5.0.1 on 2024-02-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingaccount',
            name='account_number',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tradingaccount',
            name='client_group',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
