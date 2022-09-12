from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Stock


@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'is_deleted')
    list_display_links = ("name",)
    ordering = ['-id']
