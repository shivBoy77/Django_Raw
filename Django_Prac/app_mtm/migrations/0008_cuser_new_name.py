# Generated by Django 3.2.2 on 2021-05-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mtm', '0007_cuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuser',
            name='new_name',
            field=models.CharField(default='unknown', max_length=90),
            preserve_default=False,
        ),
    ]
