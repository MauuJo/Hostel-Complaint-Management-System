from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

'''class CustomUser(AbstractUser):
    student_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255)'''

'''class StudentManager(BaseUserManager):
    def create_user(self, student_id, password=None, **extra_fields):
        if not student_id:
            raise ValueError('The Student ID must be set')
        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(student_id, password, **extra_fields)

class Student(AbstractBaseUser):
    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    hostel = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['full_name', 'email', 'phone', 'hostel', 'room_no']

    def __str__(self):
        return self.student_id

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff'''

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    class Meta:
        db_table='category'

class staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Consider using Django's built-in authentication system
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    class Meta:
        db_table='staff'

class hostel(models.Model):
    hostel_id = models.AutoField(primary_key=True)
    hostel_name = models.CharField(max_length=255)
    class Meta:
        db_table='hostel'

class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Consider using Django's built-in authentication system
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    class Meta:
        db_table='student'
    
    def save(self, *args, **kwargs):
        # Call the superclass save method to perform the actual saving
        super().save(*args, **kwargs)

class complaint(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE) 
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE) 
    student = models.ForeignKey(student, on_delete=models.CASCADE) 
    staff = models.ForeignKey(staff, on_delete=models.CASCADE) 
    description = models.TextField()
    room_no = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table='complaint'
