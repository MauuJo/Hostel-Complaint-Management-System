# Generated by Django 5.0.3 on 2024-03-14 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hostel_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_no', models.IntegerField()),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.hostel')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('room_no', models.IntegerField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.category')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.hostel')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.staff')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempapp.student')),
            ],
        ),
    ]
