# Generated by Django 4.2.1 on 2024-03-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_account_app', '0013_alter_tradingproduct_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradingproduct',
            name='group',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
