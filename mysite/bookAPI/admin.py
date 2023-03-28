from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Book


# Register your models here.



class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'rating', 'image']

admin.site.register(Book, BookAdmin)  