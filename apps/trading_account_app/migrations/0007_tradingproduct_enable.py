# Generated by Django 4.2.4 on 2024-02-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_account_app', '0006_alter_tradingproduct_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingproduct',
            name='enable',
            field=models.BooleanField(default=True),
        ),
    ]
