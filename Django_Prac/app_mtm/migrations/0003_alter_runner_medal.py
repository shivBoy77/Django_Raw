# Generated by Django 3.2.2 on 2021-05-09 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mtm', '0002_alter_runner_medal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='medal',
            field=models.CharField(choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze'), ('WIN', 'Win'), ('LOSE', 'Lose')], max_length=10),
        ),
    ]