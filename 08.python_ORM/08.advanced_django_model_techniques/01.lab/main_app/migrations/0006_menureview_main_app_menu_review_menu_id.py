# Generated by Django 5.0.4 on 2024-07-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_menureview'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='menureview',
            index=models.Index(fields=['menu'], name='main_app_menu_review_menu_id'),
        ),
    ]
