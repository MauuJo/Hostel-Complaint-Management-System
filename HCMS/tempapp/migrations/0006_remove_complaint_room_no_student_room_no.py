# Generated by Django 5.0.3 on 2024-04-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempapp', '0005_remove_student_room_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='room_no',
        ),
        migrations.AddField(
            model_name='student',
            name='room_no',
            field=models.IntegerField(default=0),
        ),
    ]
