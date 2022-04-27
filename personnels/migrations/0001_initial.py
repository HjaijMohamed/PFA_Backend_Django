# Generated by Django 3.2.12 on 2022-03-15 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.IntegerField(default=55)),
                ('nom', models.CharField(default='', max_length=70)),
                ('prenom', models.CharField(default='', max_length=200)),
                ('date_nais', models.DateField(blank=True, null=True)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(default='email@email.com', max_length=254)),
                ('heure_trav', models.TimeField(blank=True, null=True)),
                ('img', models.ImageField(default='images/inconnu.jpg', upload_to='images')),
            ],
        ),
    ]
