# Generated by Django 5.0.1 on 2024-02-01 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_bankdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_app.personaldetail'),
        ),
    ]
