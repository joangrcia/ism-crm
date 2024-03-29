# Generated by Django 4.2.1 on 2024-03-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_app', '0015_alter_ibaccount_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ibaccount',
            old_name='is_confirmed',
            new_name='is_ib',
        ),
        migrations.AddField(
            model_name='ibaccount',
            name='is_sub_ib',
            field=models.BooleanField(default=False),
        ),
    ]
