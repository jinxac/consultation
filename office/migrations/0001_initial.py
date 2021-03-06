# Generated by Django 3.0.3 on 2020-03-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('street_address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
