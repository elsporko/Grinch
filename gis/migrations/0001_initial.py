# Generated by Django 4.1.7 on 2023-08-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=140)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
    ]
