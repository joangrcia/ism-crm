# Generated by Django 4.2.4 on 2024-02-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_account_app', '0005_tradingproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradingproduct',
            name='group',
            field=models.CharField(default=''),
        ),
    ]