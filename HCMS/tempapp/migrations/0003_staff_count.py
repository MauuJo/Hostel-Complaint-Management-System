# Generated by Django 5.0.3 on 2024-04-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempapp', '0002_alter_complaint_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]