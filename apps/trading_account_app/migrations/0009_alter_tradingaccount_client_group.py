# Generated by Django 4.2.4 on 2024-02-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_account_app', '0008_alter_tradingaccount_client_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradingaccount',
            name='client_group',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]