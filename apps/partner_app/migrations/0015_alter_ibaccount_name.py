# Generated by Django 4.2.1 on 2024-03-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_app', '0014_alter_ibaccount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ibaccount',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]