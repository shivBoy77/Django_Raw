# Generated by Django 3.2.2 on 2021-05-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mtm', '0003_alter_runner_medal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='app_mtm.Publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
