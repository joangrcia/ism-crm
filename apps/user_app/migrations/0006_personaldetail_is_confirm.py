# Generated by Django 4.2.4 on 2024-02-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_bankdetail_swift_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='is_confirm',
            field=models.BooleanField(default=False),
        ),
    ]
