# Generated by Django 4.2.3 on 2023-08-01 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KR')),
                ('business_file', models.FileField(upload_to='business/')),
                ('registration_file', models.FileField(upload_to='registration/')),
                ('logo', models.ImageField(upload_to='logo/')),
                ('info_file', models.FileField(upload_to='info/')),
                ('public', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=8)),
                ('img', models.ImageField(blank=True, null=True, upload_to='menu_img/')),
                ('exp', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.menucategory')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr', models.ImageField(blank=True, null=True, upload_to='qrcode/')),
                ('categories', models.ManyToManyField(blank=True, null=True, related_name='categories', to='sellers.menucategory')),
                ('register', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.register')),
            ],
        ),
    ]
