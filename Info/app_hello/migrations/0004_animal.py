# Generated by Django 2.2 on 2021-05-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hello', '0003_auto_20210430_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legs', models.IntegerField()),
            ],
            options={
                'db_table': 'Pets',
            },
        ),
    ]