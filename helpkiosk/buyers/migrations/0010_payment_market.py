# Generated by Django 4.2.3 on 2023-08-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0006_option'),
        ('buyers', '0009_cartitem_options_paymentitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.market'),
        ),
    ]
