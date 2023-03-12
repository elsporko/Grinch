# Generated by Django 4.1.7 on 2023-03-02 02:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RouteNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PickList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField(default=0)),
                ('PickupDate', models.DateField(default='2023-01-01')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('homephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('streetaddress', models.CharField(max_length=100)),
                ('whereisit', models.CharField(blank=True, max_length=30, null=True)),
                ('gotmoney', models.BooleanField(default=False)),
                ('gottree', models.BooleanField(default=False)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='picklist.route')),
            ],
        ),
    ]
