from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(Document)
class Document_Admin(ImportExportModelAdmin):
    pass
