from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(Student)
class Student_Admin(ImportExportModelAdmin):
    search_fields = ['name','id_student','last_name']
    list_filter = ['upload_date']
    list_display = ['full_name','upload_date']
    ordering = ['upload_date']
