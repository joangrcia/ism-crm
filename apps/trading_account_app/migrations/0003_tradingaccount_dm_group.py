# Generated by Django 4.2.1 on 2024-03-09 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
        ('trading_account_app', '0002_remove_tradingaccount_dm_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingaccount',
            name='dm_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_app.producttrading'),
            preserve_default=False,
        ),
    ]
