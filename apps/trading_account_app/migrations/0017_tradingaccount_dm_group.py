# Generated by Django 4.2.1 on 2024-03-07 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading_account_app', '0016_producttrading'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingaccount',
            name='dm_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trading_account_app.producttrading'),
            preserve_default=False,
        ),
    ]
