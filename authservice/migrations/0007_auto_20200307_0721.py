# Generated by Django 3.0.3 on 2020-03-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authservice', '0006_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=1, verbose_name=[(0, 'Doctor'), (1, 'Assistant'), (2, 'Client'), (3, 'Admin')]),
        ),
    ]
