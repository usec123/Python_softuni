# Generated by Django 5.0.4 on 2024-07-14 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_driver_drivinglicense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivinglicense',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='license', to='main_app.driver'),
        ),
    ]
