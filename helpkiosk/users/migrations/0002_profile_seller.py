# Generated by Django 4.2.3 on 2023-08-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seller',
            field=models.BooleanField(default=False),
        ),
    ]