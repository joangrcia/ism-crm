# Generated by Django 4.2.1 on 2024-03-28 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trading_account_app', '0003_tradingaccount_dm_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('bank_method', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted')], max_length=10)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('account', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='trading_account_app.tradingaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('bank_method', models.CharField(max_length=10)),
                ('is_confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('account', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='trading_account_app.tradingaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IntTransHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('status', models.CharField(choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted')], max_length=10)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('from_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transfers_from_history', to='trading_account_app.tradingaccount')),
                ('to_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transfers_to_history', to='trading_account_app.tradingaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IntTrans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('is_confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('from_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transfers_from_inttrans', to='trading_account_app.tradingaccount')),
                ('to_account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transfers_to_inttrans', to='trading_account_app.tradingaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('bank_method', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted')], max_length=10)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('account', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='trading_account_app.tradingaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('bank_method', models.CharField(max_length=10)),
                ('is_confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('account', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='trading_account_app.tradingaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]