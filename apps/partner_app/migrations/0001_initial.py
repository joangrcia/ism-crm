# Generated by Django 4.2.1 on 2024-03-28 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trading_account_app', '0003_tradingaccount_dm_group'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IbAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('is_confirm', models.BooleanField(default=False)),
                ('is_ib', models.BooleanField(default=False)),
                ('is_sub_ib', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('account_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trading_account_app.tradingaccount')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MibAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MibList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ib_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partner_app.ibaccount')),
                ('mib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner_app.mibaccount')),
            ],
        ),
        migrations.CreateModel(
            name='IbList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ib_lists', to=settings.AUTH_USER_MODEL)),
                ('ib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner_app.ibaccount')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted')], max_length=10)),
                ('request', models.CharField(choices=[('IB', 'IB'), ('SUB IB', 'SUB IB'), ('MIB', 'MIB')], max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
