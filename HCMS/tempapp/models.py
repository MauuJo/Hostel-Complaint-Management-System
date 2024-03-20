from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Consider using Django's built-in authentication system
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Hostel(models.Model):
    hostel_id = models.AutoField(primary_key=True)
    hostel_name = models.CharField(max_length=255)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Consider using Django's built-in authentication system
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_no = models.IntegerField()

class Complaint(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    description = models.TextField()
    room_no = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
