# Generated by Django 3.0.3 on 2020-03-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20200305_1525'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Specialization',
        ),
        migrations.AlterField(
            model_name='doctoravailability',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='doctoravailability',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
