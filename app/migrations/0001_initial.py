# Generated by Django 5.0.2 on 2024-02-28 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DosageDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('working_hours', models.CharField(max_length=100)),
                ('dose', models.ManyToManyField(to='app.dosagedetail')),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(default='', max_length=150)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vaccinationcenter')),
            ],
        ),
    ]