# Generated by Django 4.2.1 on 2024-03-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_app', '0016_rename_is_confirmed_ibaccount_is_ib_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ibaccount',
            name='is_ib',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='ibaccount',
            name='is_sub_ib',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
