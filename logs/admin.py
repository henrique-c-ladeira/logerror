from django.contrib import admin
from .models import ErrorLog


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'datetime', 'message')


# Register your models here.
admin.site.site_header = "Error Logs"
admin.site.site_title = "Error Logs"
admin.site.index_title = "Error Logs"
admin.site.site_url = None
