# Generated by Django 4.2.1 on 2024-03-09 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_producttrading_is_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttrading',
            old_name='is_number',
            new_name='is_enable',
        ),
    ]