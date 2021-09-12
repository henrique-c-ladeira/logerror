from django.contrib import admin
from .models import ErrorLog


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'datetime', 'message')
    list_per_page = 50
    list_filter = ('app_name', 'datetime')
    search_fields = ['app_name']


# Register your models here.
admin.site.site_header = "Error Logs"
admin.site.site_title = "Error Logs"
admin.site.index_title = "Error Logs"
admin.site.site_url = None
