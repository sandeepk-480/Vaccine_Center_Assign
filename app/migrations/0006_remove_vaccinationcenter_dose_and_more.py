# Generated by Django 5.0.2 on 2024-02-28 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_vaccinationcenter_dose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinationcenter',
            name='dose',
        ),
        migrations.AddField(
            model_name='dosagedetail',
            name='center_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.vaccinationcenter'),
        ),
    ]
