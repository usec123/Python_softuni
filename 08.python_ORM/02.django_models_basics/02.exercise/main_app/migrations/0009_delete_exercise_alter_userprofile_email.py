# Generated by Django 5.0.4 on 2024-06-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_exercise'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='students@softuni.bg', max_length=254, unique=True),
        ),
    ]
