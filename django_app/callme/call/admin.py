from django.contrib import admin
from .models import CallRequest


class CallRequestAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'your_name', 'your_phone_number', 'call_status')
    list_filter = ('your_name', 'your_phone_number', 'call_status')


admin.site.register(CallRequest, CallRequestAdmin)
# Register your models here.
