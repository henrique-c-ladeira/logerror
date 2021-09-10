from django.contrib import admin
from .models import ErrorLog

# Register your models here.
admin.site.register(ErrorLog)
admin.site.site_header = "Error Logs"
admin.site.site_title = "Error Logs"
admin.site.index_title = "Error Logs"
admin.site.site_url = None
