# Generated by Django 5.0.4 on 2024-07-18 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mage',
            old_name='assassination_technique',
            new_name='spellbook_type',
        ),
    ]
