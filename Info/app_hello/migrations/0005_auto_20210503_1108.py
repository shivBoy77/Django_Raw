# Generated by Django 2.2 on 2021-05-03 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hello', '0004_animal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Pet'},
        ),
    ]
