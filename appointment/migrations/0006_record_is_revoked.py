# Generated by Django 3.0.3 on 2020-03-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20200304_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='is_revoked',
            field=models.BooleanField(default=False),
        ),
    ]
