# Generated by Django 4.2.4 on 2024-02-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]