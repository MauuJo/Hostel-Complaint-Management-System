from django.contrib import admin
from .models import category, staff, hostel, student, complaint

# Register your models here.
admin.site.register(category)
admin.site.register(staff)
admin.site.register(hostel)
admin.site.register(student)
admin.site.register(complaint)
