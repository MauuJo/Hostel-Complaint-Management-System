from django.contrib import admin
from .models import Category, Staff, Hostel, Student, Complaint

# Register your models here.
admin.site.register(Category)
admin.site.register(Staff)
admin.site.register(Hostel)
admin.site.register(Student)
admin.site.register(Complaint)
