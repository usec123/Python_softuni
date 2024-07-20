# Generated by Django 5.0.4 on 2024-07-20 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[a-zA-Z ]*', message='Name can only contain letters and spaces')])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18, message='Age must be greater than or equal to 18')])),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address')])),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('[+]359[*]{9}', message="Phone number must start with '+359' followed by 9 digits")])),
                ('website_url', models.URLField(validators=[django.core.validators.URLValidator(message='Enter a valid URL')])),
            ],
        ),
    ]
