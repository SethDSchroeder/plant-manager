# Generated by Django 5.0.7 on 2024-08-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greenhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('temp', models.IntegerField()),
                ('humidity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('scientific_name', models.CharField(max_length=50)),
                ('location', models.IntegerField()),
                ('soil_moisture', models.IntegerField()),
            ],
        ),
    ]
