# Generated by Django 3.2.12 on 2022-03-20 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conge',
            old_name='date_retour',
            new_name='date_fin',
        ),
    ]
