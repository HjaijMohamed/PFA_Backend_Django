# Generated by Django 3.2.12 on 2022-03-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='id',
        ),
        migrations.AlterField(
            model_name='personnel',
            name='cin',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
